import argparse
import json

from docxtpl import DocxTemplate, RichText
from dotmap import DotMap
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .globals import raise_helper
from .filters import to_datetime


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
    parser_init.add_argument(
        "-o",
        "--output-file",
        help="path to docx file to output the rendered resume into",
        required=True,
    )
    args = parser.parse_args()
    if args.command == "init":
        # 'x' mode opens the file for exclusive creation, failing if the file already exists.
        # See https://docs.python.org/3/library/functions.html#open
        with open(args.resume_file, "x"):
            pass
    elif args.command == "render":
        # Create the Jinja2 environment
        env = Environment(
            extensions=["jinja2.ext.do"],
            autoescape=select_autoescape(),
            loader=FileSystemLoader("."),
        )
        # Define the policies (see https://jinja.palletsprojects.com/en/3.0.x/api/#policies)
        env.policies["json.dumps_kwargs"] = {}
        # Define the globals
        env.globals["raise"] = raise_helper
        # Define the filters
        env.filters["from_json"] = json.loads
        env.filters["to_datetime"] = to_datetime
        env.filters["dotmap"] = DotMap
        # Render the template
        template = DocxTemplate(template_file)
        env.globals["template"] = template
        env.globals["RichText"] = RichText
        template.render(context=context, jinja_env=env)
        template.save(args.output)
    else:
        raise RuntimeError(f"Unrecognized command: {args.command}")


if __name__ == "__main__":
    cli()


#     # Add contents of files passed in with --file to the context
#     for key, file in (args.file or dict()).items():
#         context[key] = "".join(fileinput.input(files=[file]))
#     # Process the template file
#     template_file = Path(args.template_file)
#     if template_file.suffix == ".docx":
#         # Use python-docx-template
#         if not args.output:
#             raise RuntimeError("Using a docx template requires an output file to be provided with --output.")
#         try:
#         except ImportError:
#             raise ImportError("Install jinjai with [docx] option to use docx templates.")
#         template = DocxTemplate(template_file)
#         env.globals["template"] = template
#         env.globals["RichText"] = RichText
#         template.render(context=context, jinja_env=env)
#         template.save(args.output)
