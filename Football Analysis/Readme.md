Project Title: Football Video Analysis

Project Overview

This project aims to analyze football videos by detecting and tracking players, referees, and the ball. The following key steps are involved:

Manual Annotation:

A football dataset was manually annotated to provide ground truth information for object detection and tracking.
Annotations included bounding boxes for players, referees, and the ball.
Team Identification:

K-Means clustering was employed to group players into two teams based on their spatial proximity and motion patterns.
Siglip, a powerful feature extraction model, was utilized to extract relevant features for clustering.
Real-Time Tracking:

YOLOv11, a state-of-the-art object detection and tracking model, was implemented to assign unique IDs to each detected object (player, referee, or ball).
This enables accurate tracking of objects across video frames.
Dataset

A custom football video dataset was created and manually annotated.
The dataset includes a variety of football match scenarios, covering different playing conditions and camera angles.
Model Architecture

Siglip: A feature extraction model used for K-Means clustering.
YOLOv11: A real-time object detection and tracking model for player and object identification.
Implementation Details

Data Preparation:
Annotated data was pre-processed to extract relevant information for training and testing.
Data augmentation techniques were applied to increase the diversity of the dataset.
Model Training:
Siglip and YOLOv11 models were trained on the annotated dataset using appropriate loss functions and optimization algorithms.
Model hyperparameters were tuned to achieve optimal performance.
Inference and Tracking:
The trained YOLOv11 model was used to detect and track objects in real-time.
K-Means clustering was applied to assign players to teams based on their extracted features.
Tracking information was visualized using appropriate visualization techniques.
Future Work

Explore advanced tracking algorithms to improve accuracy and robustness.
Incorporate additional features like player attributes (jersey number, position) for more detailed analysis.
Develop a user interface to visualize and analyze the tracking results.
Apply the system to a larger dataset to evaluate its performance in diverse scenarios.
Acknowledgements

We would like to thank the contributors who helped with data annotation and model development.

Contact

[Your Name]
[Your Email]
[Your Affiliation]