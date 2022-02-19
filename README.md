# Growth Project

## About The Project

[![Braze Logo][braze-logo]](https://braze.com)

This is the take home project for Braze's Growth team. I time-boxed myself approximately six hours for this project. A rough breakdown of effort looks like:

- 2 hours to play with the API and read the documentation
- 2 hours to learn the basics of Flask and Bootstrap
- 2 hours to create the application and display the data

See the "Assumptions" and "Roadmap" sections below for more information about design decisions and what I would have done given more time.

### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Bootstrap](https://getbootstrap.com/)

## Getting Started

Follow these steps to get this application running locally.

### Prerequisites

This project requires Python3. See: https://www.python.org/downloads/

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation

1. Follow up with your Customer Success representative to get your company's API key.
2. Clone the repo
   ```sh
   git clone https://github.com/jonathanlao/growth_project.git
   ```
3. Install packages with `pip`
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API key in `.flask_env`
   ```sh
   API_KEY='ENTER YOUR API';
   ```
5. Run the application
   ```sh
   flask run
   ```
6. View the application by navigating to http://localhost:5000/

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

See the requirements listed [here](https://confluence.braze.com/pages/viewpage.action?spaceKey=GROW&title=Interview+Loop+for+Growth+Engineer) (Braze SSO required).

<p align="right">(<a href="#top">back to top</a>)</p>


## Assumptions

1. The landing page includes only non-archived campaigns. 
2. An individual campaign page only includes the last 30 days worth of analytics.
3. According to the [get_campaign_analytics](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_analytics/) documentation, 
"All push message types will have the same statistics shown for `android_push` above." The image shows `sent`, `direct_opens`, `total_opens`, `bounces`, and `body_clicks`.
That seemed like good baseline stats to show for each channel and therefore that is what analytics are displayed. But according to [other documentation](https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics/),
as well as judging by the actual response data I was getting back, that seems to not actually be the case. Moreover, I'm not sure what "body click" would even mean for a channel like email.
4. The assignment instructions seemed to perhaps imply that "relevant stats" should appear in a single dashboard page. However, there did not seem to be an easy way to get statistics for multiple camapgins in a single API call.
Rather than getting analytics for every campaign listed all at once (which could be a lot of API calls), I chose to design it such that the user needs to click on a campaign to view more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

### Current Roadmap

- [x] Landing Page
- [x] Campaign details and analytics page
- [x] Landing page download button
- [x] README
- [x] Filter and search
- [ ] Product Feedback

### Given More Time
- [ ] Separate filter for tags using a dropdown
- [ ] Specify a date range for metrics
- [ ] Aggregate stat details, like total opens overall

### Deprioritized

- [ ] Better front-end design
- [ ] Separating css and js files

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Your Name - [@Braze](https://twitter.com/Braze) - jonathan.lao@braze.com

Project Link: [https://github.com/jonathanlao/growth_project](https://github.com/jonathanlao/growth_project)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Thanks to the following resources, without whom, this project could not be possible.

* [Miguel Grinberg's Mega Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [othneildrew's Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Braze](https://www.braze.com)

<p align="right">(<a href="#top">back to top</a>)</p>

[braze-logo]: braze.png
