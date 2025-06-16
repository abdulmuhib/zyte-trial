# Zyte-trial

## Scrapy Cloud Project URL
https://app.zyte.com/p/816528/jobs

## Project description

I have used [scrapy](https://scrapy.org) and [Zyte API](https://www.zyte.com/zyte-api) to download books data from [books.toscrape.com](http://books.toscrape.com), , which contains data about 1000 books and quotes data from [quotes_toscrape_com](http://quotes.toscrape.com/scroll) , which contains data about 90 quotes.

This repository contains a main folder **trial** which contains multiple sub-directories as follows: 

1. `constants`  contains predefined values used across the spiders. Defining these constants in separate classes enhances scalability and maintainability. If a field name or selector changes in the future, updates can be made centrally within the constants, without modifying the spider logic itself—ensuring cleaner, more robust, and future-proof code.

2. `items` contains the [Scrapy Items](https://docs.scrapy.org/en/latest/topics/items.html) for spiders.

3. `middlewares` contains the [Spider Middlewares](https://docs.scrapy.org/en/latest/topics/spider-middleware.html) for the spiders.

4. `pipelines` contains [Scrapy Items](https://docs.scrapy.org/en/latest/topics/items.html) for their respective spiders and we are doing data cleaning in these pipelines.

5. `spiders` contains the [Spiders](https://docs.scrapy.org/en/latest/topics/spiders.html).

## Zyte API Usage in Spiders
Each spider overrides its own settings to allow for customized configurations tailored to specific scraping needs, while preserving the base settings. This approach ensures flexibility and modularity without impacting the global configuration.

1. `bookspider` I have used the Zyte API for [Browser HTML](https://docs.zyte.com/zyte-api/usage/browser.html#browser-html) mode.

2. `quotespider` I used the Zyte API for [Actions](https://docs.zyte.com/zyte-api/usage/browser.html#actions) as I have to scroll.

## Getting started

First of all, `fork` this repo and then `clone` your fork to have a local copy.
```
$ cd zyte-trial
```
create a virtual envirnment
```
$ python -m venv venv
```
and then activate it with
```
$ venv\Scripts\activate
```  
Then install the requirements from requirements.txt
```
$ pip install -r requirements.txt
```
##### Note: Replace 'your_zyte_api_key' with your Zyte API key in settings.txt
```
$ scrapy crawl <spider_name>
``` 
Again, you can save the data with the `-o filename.format` optional argument.

## Get Started With Scrapy Cloud

Getting started with Scrapy Cloud is very simple.

First create a [Free Account Scrapy Cloud Here](https://app.zyte.com/account/signup/scrapycloud), and then once logged in click "Start a new project".

![image](https://github.com/user-attachments/assets/1417eb9d-ed4b-4cdf-8e26-a646bfdbdfad)

And give your project a name.

![image](https://github.com/user-attachments/assets/aef7e4de-21a4-4e5c-8bd6-10c14d3a75f2)

Once your project has been created, you have two ways to deploy your Scrapy spiders to Scrapy Cloud:

Via the Command Line
Via Github Integration

![image](https://github.com/user-attachments/assets/2a258385-f356-4cc2-8f69-b1420d2048fd)

### Deploy Your Spiders To Scrapy Cloud From Command Line

Using the shub command line tool we can deploy our spiders directly to Scrapy Cloud from the command line.

First install shub on your system:
```
$ pip install shub
``` 
Then link the shub client to your Scrapy Cloud project by running shub login in your command line, and when prompted enter your Scrapy Cloud API key.
```
$ shub login
API key: YOUR_API_KEY
``` 
You can find your API key on the Code & Deploys page.

Add scrapinghub.yml with the following content into your project:
```
requirements:
  file: requirements.txt
stacks:
  default: scrapy:2.11-20241022
```
##### Note: Replace "your_project_id" with your project id in "scrapy.cfg" and "scrapinghub.yml"

Then to deploy your Scrapy project to Scrapy Cloud, run the shub deploy command followed by your project's id:

```
shub deploy PROJECT_ID
```
You can find your project's id, on the Code & Deploys page or in the project URL.
```
https://app.zyte.com/p/PROJECT_ID/jobs
```
If successful, you will see the spiders you have available in the spiders tab.

![image](https://github.com/user-attachments/assets/3875a576-a50c-4ebe-a45b-e4eb90a60a00)

You can then run your scraping job on Scrapy Cloud directly from your command line:
```
$ shub schedule bookspider 
Spider bookspider scheduled, watch it running here:
https://app.zyte.com/p/PROJECT_ID/job/1/8
```
### Deploy Your Spiders To Scrapy Cloud via GitHub

The other option is to connect Scrapy Cloud directly to your GitHub account and deploy your spiders directly from the GitHub.

On the Code & Deploys page, select the option to Connect to Github and follow the instructions.

If you haven't connected Zyte to your GitHub account previously, then you might be asked to authorize Zyte to access your repositories.

![image](https://github.com/user-attachments/assets/a1982973-021c-4e2b-b7da-db6ba955e062)

Next, you will be prompted to pick which repository you want Scrapy Cloud to connect to.

![image](https://github.com/user-attachments/assets/de55b817-0d72-4441-9727-5fcaf23ac854)
```
tip
The repository you select must contain a Scrapy project at its root (i.e. the scrapy.cfg file is located in the repository root). Otherwise, the build process will fail.
```
By default, when you connect Scrapy Cloud to a GitHub repository it is configured to auto-deploy any changes you push to the repository. However, if you prefer you can switch it to Manual Deploy mode, and deploy changes to your spiders manually.

If you leave it in Automatic Deploy mode, then to commence the first deployment then click on the Deploy Branch button.

![image](https://github.com/user-attachments/assets/2698f0f6-c798-4bbe-a47d-181ad15321b6)

If successful, you will see the spiders you have available in the spiders tab.

![image](https://github.com/user-attachments/assets/9384a793-cb67-444a-9120-25b1bc8b8af7)




