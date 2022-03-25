# Predict Voter Propensity with a Linear Regression Model

![cover image](cover_image.jpg)

### About

Running for office is a daunting task, especially for candidates who have never run before. During the campaign, candidates have to convince as many people as possible to vote for them. There’s never enough time or money, so candidates have to be efficient and focus on the voters who actually vote. But is it possible to predict which voter is more likely to go to the polls?

This project explores some publicly available voting data to to learn more information about a group of voters, and to use data ro predict voting propensity.

This repository supplements the [Use voter data… win elections!](https://medium.com/@lajos.kamocsay/use-voter-data-win-elections-e9a68862cbed) story on [medium](https://medium.com/@lajos.kamocsay/use-voter-data-win-elections-e9a68862cbed).

### Installation

This project uses [jupyter](https://jupyter.org/) notebooks. The **requirements.txt** file contains information about required packages. Create a [conda](https://anaconda.org/) environment with all required packages:

`conda create --name <env> --file requirements.txt`

### Files in this repository

**/data/voting_data_anonymized.tsv** - anonimized public voting data in tab separated format
**a quick look at the data.ipynb** - notebook exploring the data
**linear regression.ipynb** - notebook with data preparation, linear regression modeling and prediction testing
**/cover_image** folder containing illustrations and a python file to create the randomized cover image

### Acknowledgements

https://pixabay.com/users/coffeebeanworks-558718/ - illustrations used in cover image by coffeebeanworks

https://github.com/appeler/ethnicolr - name based data labeling for race and color

