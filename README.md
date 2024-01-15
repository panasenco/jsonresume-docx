# jsonresume-docx
Render your JSON resume as a .docx file.
Blend in with the corporate drones.
Use for job applications where a colorful resume that showcases your technical proficiency would be showing a little too much personality. ;)

## Usage
1.  Download the file resume-template.docx from this repo to your computer.
2.  If you don't already have a [JSON resume](https://jsonresume.org/), download the file sample-resume.json from this repo.
    Rename the file to resume.json.
    Modify the file with your own information.
3.  Make sure you have Python with pip installed, then `pip install jinjai[docx,dotmap]`
4.  Run the command:
    ```
    jinjai resume-template.docx -f resume=resume.json -o resume.docx
    ```
5.  You now have a .docx file with all your details filled out!

## Acknowledgements
Huge **thank you** to Colin McIntosh of [SheetsResume.com](https://sheetsresume.com/) for freely sharing the docx template this is based on.
I originally found the template in Colin's [massively popular post in r/jobs](https://www.reddit.com/r/jobs/comments/7y8k6p/im_an_exrecruiter_for_some_of_the_top_companies/).