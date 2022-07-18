## About The Project

The goal of the project is to solve a test task to filter incorrect points in the kml file and calculate the total distance.

![service](https://user-images.githubusercontent.com/62716305/179479091-018cb6d0-1ecf-44d6-8412-ddbeda2a50f7.png)

## Getting Started

The project is a small web service written with **Flask**. It is completely wrapped in **docker-compose**, which allows you to deploy it quickly and without much trouble.

### Prerequisites

- docker-compose
- python > 3.5

The other dependencies, along with their versions, are listed in the **requirements.txt** file.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ivanelgran23/vehicle_track.git
   ```
2. Build and run service
   ```sh
   sudo docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
   ```

## Usage

1. After launching the service, go to http://localhost:8383/.
2. Upload the KML file via the form on the website and click the "Upload" button.
3. You will be taken to the main page. On the left will be an interactive map with the track drawn, and on the right a set of available filters with parameters. All parameters are set to optimal values and you can simply click on the "Apply Filters" button.
4. After a short amount of time, the map will update with a new rendered track, and the total length of the distance traveled will also change, located under the map.
5. To reset filters and start over, click the "Reset filters" button.

## Filtering logic

- We need to reduce the dimensionality of the set of coordinates, to improve the work of the filtering algorithms. To do this, the first step I remove full duplicate coordinates from the file.
- Also, I use the [Ramer-Douglas-Peucker](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm) algorithm to build a similar track but with fewer points. By changing the epsilon parameter, we change the dimensionality of the distance between the approximating segment and the points on the curve. As a result, we get almost the same track, but with a much smaller number of points: 4500 -> 650.
- We need to remove the outliers from the track. In order to **remove groups of points** that lie outside the track, I use the [DBSCAN](https://towardsdatascience.com/how-dbscan-works-and-why-should-i-use-it-443b4a191c80) clustering algorithm. Using it, I will select the largest cluster, which is the entire track, and small groups of points, will be marked as other clusters and removed. The parameter epsilon is automatically calculated, but you can change the minimum number of points that form a cluster.
- To **remove single outliers**, I use the [law of cosines](https://en.wikipedia.org/wiki/Law_of_cosines). The angle between the three coordinates is calculated, and if the angle is too sharp - then this point either lies outside the track, or is insignificant for measurements, because the car can not make such maneuvers. You can also change the minimum threshold angle.
- And at the end, to **smooth** out the entire track, I use the [Kalman filter](https://en.wikipedia.org/wiki/Kalman_filter). You can adjust the number of iterations of the algorithm to enhance the averaging of coordinate values in the track, but too large a parameter will distort it.

## Improvements

In addition to experimenting with parameters, you can use the [map matching](https://en.wikipedia.org/wiki/Map_matching) algorithm, which correlates GPS data with a real road map. In this way, you can get a nearly perfect GPS path tracking.

## Contact

Medvedev Ivan - anonelgran@mail.ru

Project Link: [https://github.com/ivanelgran23/vehicle_track.git](https://github.com/ivanelgran23/vehicle_track.git)

<p align="right">(<a href="#top">back to top</a>)</p>




