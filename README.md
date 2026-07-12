# About the Project

This tiny GUI app gets news from the web via <a href="https://newsapi.org">News API</a> and shows or emails the requested news.

# Getting Started

1. Clone the project to your machine by running the following command:

    `git clone https://github.com/Alireza3044/news-fetcher.git`

2. Run the command `python -r requirements.txt` to install the required packages.

3. Create an account on the <a href="https://newsapi.org">News API</a>'s website.

4. Create a `.env` file in the projects root directory and create the following variables:

    `API_KEY`
    
    `SERVER_HOST_NAME`    
    
    `SERVER_HOST_PORT`
    
    `SERVER_EMAIL_USERNAME`
    
    `SERVER_EMAIL_PASSWORD`

5. Provide your API key to `API_KEY` variable, and your hosting server's name and port to `SERVER_HOST_NAME` and `SERVER_HOST_PORT`. An example could be `smtp.gmail.com` with port `465`. Also a valid `SERVER_EMAIL_USERNAME` and `SERVER_EMAIL_PASSWORD` should be provided.

6. Now run the GUI by `python main.py`.
