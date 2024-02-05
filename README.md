# jsonresume-docx
Render your JSON resume as a .docx file, hide your personality. ;)

## Installation

```
pipx install git+https://github.com/panasenco/jsonresume-docx.git
```

## Initialize a resume

```
jsonresume-docx init --resume-file resume.json
```

Note that jsonresume-docx introduces some padding fields in work > experience sections:
- _startDatePad: Number of spaces to insert between the employer name and the start date.
  Note: Only the _startDatePad from the **latest** position of an employer is used.
- _locationPad: Number of spaces to insert between the latest position name and the location.
  Note: Only the _locationPad from the **latest** position of an employer is used.

Modify the file with your own information.
Pay attention to these padding fields as they can make or break the appearance of your resume.

## Usage

To render a file called resume.docx from a file called resume.json:

```
jsonresume-docx render --resume-file resume.json --output-file resume.docx
```

You now have a .docx file with all your details filled out!

## Acknowledgements
Huge **thank you** to Colin McIntosh of [SheetsResume.com](https://sheetsresume.com/) for freely sharing the docx template this is based on.
I originally found the template in Colin's [massively popular post in r/jobs](https://www.reddit.com/r/jobs/comments/7y8k6p/im_an_exrecruiter_for_some_of_the_top_companies/).