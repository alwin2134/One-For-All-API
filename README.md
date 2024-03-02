# One-For-All API Documentation

<!--
![GitHub repo size](https://img.shields.io/github/repo-size/alwin2134/One-For-All-API)
![GitHub contributors](https://img.shields.io/github/contributors/alwin2134/One-For-All-API)
-->
![GitHub stars](https://img.shields.io/github/stars/alwin2134/One-For-All-API?label=Stars)
![GitHub forks](https://img.shields.io/github/forks/alwin2134/One-For-All-API?label=forks)

## Description

This repository contains documentation for the One-For-All API, a versatile API that provides various functionalities such as weather data retrieval, text generation, market data analysis, news article retrieval, and movie details lookup.

## Table of Contents

- [Getting Started](#getting-started)
- [Weather Branch](#weather-branch)
- [ChatGPT Branch](#chatgpt-branch)
- [Market Data Branch](#market-data-branch)
- [News Branch](#news-branch)
- [Movies Branch](#movies-branch)

## Getting Started

To get started with the One-For-All API, follow the instructions provided in the [API documentation](https://one-for-all-api.onrender.com/docs).

## Weather Branch

The Weather branch provides weather data based on the location.

### Parameters

- `api`: Your OpenWeatherMap API key.
- `location`: The location for which you want to retrieve weather data.

### Example Usage

/api/weather?api=YOUR_Openweathermap_API_KEY&location=YOUR_LOCATION


## ChatGPT Branch

The ChatGPT branch provides text generation based on the provided prompt.

### Parameters

- `api`: Your OpenAI API key.
- `prompt`: The prompt text for generating chat response.

### Example Usage

/api/chatgpt?api=YOUR_OpenAI_API_KEY&prompt=YOUR_PROMPT


## Market Data Branch

The Market Data branch provides market data based on the provided symbols.

### Parameters

- `symbols`: Comma-separated list of symbols.

### Example Usage


## Market Data Branch

The Market Data branch provides market data based on the provided symbols.

### Parameters

- `symbols`: Comma-separated list of symbols.

### Example Usage

/api/getMarketData?symbols=YOUR_SYMBOLS


## News Branch

The News branch provides news articles based on the provided sources, category, and country code.

### Parameters

- `apiKey`: Your News API key.
- `sources`: Comma-separated list of news sources.
- `category`: Category of news.
- `country`: Two-letter country code (ISO 3166-1 alpha-2).

### Example Usage

/api/news?apiKey=YOUR_API_KEY&sources=NEWS_SOURCE&category=CATEGORY&country=COUNTRY_CODE


## Movies Branch

The Movies branch provides movie details based on the provided movie title.

### Parameters

- `apiKey`: Your API key for movie data.
- `query`: The title of the movie.

### Example Usage

/api/movies?apiKey=YOUR_API_KEY&query=MOVIE_TITLE

## Example

- [Weather Example](https://github.com/alwin2134/One-For-All-API/blob/main/Examples/Weather.py)
- [ChatGPT Example](https://github.com/alwin2134/One-For-All-API/blob/main/Examples/ChatGPT.py)
- [Market Data Example](https://github.com/alwin2134/One-For-All-API/blob/main/Examples/Marke_Data.py)
- [News Example](https://github.com/alwin2134/One-For-All-API/blob/main/Examples/News.py)
- [Movies Example](https://github.com/alwin2134/One-For-All-API/blob/main/Examples/News.py)

## Contributors

Thanks to the following people who have contributed to this project:

<a href = "https://github.comalwin2134/One-For-All-API/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=alwin2134/One-For-All-API"/>
</a>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you find this project helpful, you can support its development by buying me a coffee:

<a href="https://www.buymeacoffee.com/alwin2134" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" >

<a href='https://ko-fi.com/O4O0S1UK9' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
