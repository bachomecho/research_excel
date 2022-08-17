# Researcher Tool

This tool automatically extracts the name of your research papers and the corresponding conclusion.

It then outputs them to an Excel file where you can navigate your research more easily.📈

## Install requirements

After cloning the repo, install the required modules using

```
pip install -r requirements.txt
```

## Usage

Run the main.py file.

A prompt will ask you to enter the directory where you have stored all your research papers.

![WindowsTerminal_zwcJ5uLoPG](https://user-images.githubusercontent.com/64164772/184477660-dad065d4-3b7d-4461-8199-50be10b8080b.png)

## Result

This is the output which then allows to quickly skim through your research and find what you need based on the conclusions.

![excel_screen](https://user-images.githubusercontent.com/64164772/184477665-a5b72586-a74d-4394-b393-15d65bb2d78e.png)

I will be continously working on improving functionality and speed of the script. This is the initial version which will be improved in the future.

## Next steps

1. Implement multiprocessing as the process for scanning through the whole PDF to find the word 'Conclusion' can be quite time intensive. I think multiprocessing is the way to go because the text processing requires a lot of CPU work.

2. Create an easy to use graphical interface for non-programmers as the people that can make use of this tool are mostly non-programmers.

## Contact

Feel free to contact me if you have improvement ideas.✅

Twitter: @iliamechkarov
---------------------
