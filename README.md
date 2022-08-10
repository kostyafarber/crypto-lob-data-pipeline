<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
  <h3 align="center">Order Flow Imbalance Data Pipeline</h3>

  <p align="center">
    A real-time streaming data pipeline built using Kafka and Docker. Consumes Bitcoin data from Deribit's API v2.1.1 and transforms limit order book market data to net order flow imbalance and the mid-price.
    <br />
    <a href="https://github.com/kostyafarber/crypto-lob-data-pipeline"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kostyafarber/crypto-lob-data-pipeline">View Demo</a>
    ·
    <a href="https://github.com/kostyafarber/crypto-lob-data-pipeline/issues">Report Bug</a>
    ·
    <a href="https://github.com/kostyafarber/crypto-lob-data-pipeline/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][project-image]](https://example.com)

Intially this project was intended as a starting point to build an algorithmic trading system. I decided to explore HFT (High Frequency Trading) and wanted to use Market Microstructure variables to inform my trading strategy. I wanted to use perptual cryptocurrency instruments and use order flow imbalance.

I however, instead tok the chance to change this into a fun project to practise and learn Docker and Kafka. What ultimately came of it was a simple real-time streaming data pipeline.

Please check out my [website](https://kostyafarber.github.io/projects/crpyto-perpetual-futures-kafka-streaming) for more info!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Apache Kafka](https://kafka.apache.org/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://www.docker.com/)
* [Deribit API V2.1.1](https://docs.deribit.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
### Installation

_This app was built using Docker. This solution assumes you have Docker installed on your machine_

1. Make sure you have API keys from Deribit and store them as `CLIENT_ID_DERIBIT` and `CLIENT_SECRET_DERIBIT` environment variables on your machine

1. Clone the repo

   ```sh
   git clone git@github.com:kostyafarber/crypto-lob-data-pipeline.git
   ```
2. Run the kafka and zookeeper container

   ```sh
   cd src/kafka
   docker-compose -f 'docker-compose.yml' up -d
   ```

Run the producer container

3. ```sh
    cd src/producer
    docker-compose -f 'docker-compose.yml' up 
    ```

Finally run the consumer container
  ```sh
  cd src/consumer
  docker-compose up -f `docker-compose.yml` up
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

What you should see is output that looks something like this:

![demo gif][demo-gif]

On the left is raw JSON being published to the kafka broker and on the right the JSON is being transformed with the order flow imbalance and mid-price being printed to the console.



<!-- USAGE EXAMPLES -->
## Architecture
The pipeline was built with the microservices principles in mind. Kafka, the Producer and Consumer are all in their own seperate docker containers and have no knowledge of each other apart from being on the same bridge network I defined in the `docker-compose.yml` files.

![architecture diagram][architecture-diagram]
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Add another script to make the consumer portion into a producer.

- [] Add docker youtube video in acknowledgments.

See the [open issues](https://github.com/kostyafarber/crypto-lob-data-pipeline/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kostya Farber - kostya.farber@gmail.com

Project Link: [https://kostyafarber.github.io/projects/crpyto-perpetual-futures-kafka-streaming](https://kostyafarber.github.io/projects/crpyto-perpetual-futures-kafka-streaming)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[project-image]: images/kafka.png
[demo-gif]: images/kafka-demo.gif
[architecture-diagram]: images/kafka-crypto-pipeline.png

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
