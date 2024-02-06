import argparse
import fileinput
from importlib import resources
import json
import os.path
import shutil

from docxtpl import DocxTemplate, RichText
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .filters import to_resume_date
from . import static


def cli():
    # See https://docs.python.org/3/howto/argparse.html
    parser = argparse.ArgumentParser(description="Render JSON Resume as docx file")
    # See https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers
    subparsers = parser.add_subparsers(help="command", dest="command")
    parser_init = subparsers.add_parser("init", help="create sample JSON Resume file")
    parser_init.add_argument(
        "-r",
        "--resume-file",
        help="Name of file to output sample JSON resume into. Note the file will not be overwritten.",
        required=True,
    )
    parser_render = subparsers.add_parser("render", help="render JSON Resume into docx")
    parser_render.add_argument(
        "-r",
        "--resume-file",
        help="path to JSON resume file to render to docx",
        required=True,
    )
    parser_render.add_argument(
        "-o",
        "--output-file",
        help="path to docx file to output the rendered resume into",
        required=True,
    )
    args = parser.parse_args()
    if args.command == "init":
        if os.path.exists(args.resume_file):
            raise RuntimeError(f"Destination file {args.resume_file} already exists, please remove before running init")
        # Copy the sample resume to resume_file
        sample_resume = resources.files(static) / "sample-resume.json"
        shutil.copyfile(sample_resume, args.resume_file)
    elif args.command == "render":
        # Read the resume
        resume = json.loads("".join(fileinput.input(files=[args.resume_file])))
        # Create the Jinja2 environment
        env = Environment(
            extensions=["jinja2.ext.do"],
            autoescape=select_autoescape(),
            loader=FileSystemLoader("."),
        )
        # Define the filters
        env.filters["to_resume_date"] = to_resume_date
        # Render the template
        template_file = resources.files(static) / "resume-template.docx"
        template = DocxTemplate(template_file)
        env.globals["template"] = template
        env.globals["RichText"] = RichText
        template.render(context={"resume": resume}, jinja_env=env)
        template.save(args.output_file)
    else:
        raise RuntimeError(f"Unrecognized command: {args.command}")


if __name__ == "__main__":
    cli()
