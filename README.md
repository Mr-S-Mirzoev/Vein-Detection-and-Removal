# Vein-Detection-and-Removal
The project for the idea to remove veins from a photo as after a surgical operation

## Contains:

- [Rules of collaboration](#rules)
- [Project Structure](#structure)
- [Recommended soft](#recommend)
- [Contributors](#thanks)

<a name="rules"/>

## Rules for collaboration

1) If you want to change anything in the code of `develop` branch, fork off from `develop` and name the new branch with the following prefix:

- `max-` for Maxim
- `pol-` for Pauline
- `ser-` for Sergey

After the suffix add the name for the feature you're working on. For example:

`max-vein-detection` - For the Max's code to make the vein detection module.

If we work together on some feature, we should name the branch with suffix `feature-`

2) The main development branch is `develop`. All the complete changes are being requested to merge from your feature branch to the `develop` branch and being assigned as stated in section 4.

3) The `main` and `develop` branches are never being pushed to directly. The merge requsts to `main` are requsted from `develop` only and being discussed in a team.

4) Merge requests are assigned to anyone other in a team

  For example, if Sergey wanted to merge his feature to `develop` he assignes the pull request to Pauline and Max and once whoever approves it, he merges the pull request. If the collaborator left some essential comments which should be fixed before the merge is done, the commiter fixes them and reassign to the collaborators.

5) Updates to the docs and unnecessary data can be made directly to the `develop` branch

<a name="structure"/>

## Structure of project
    
    .
    ├── articles
    │   ├── An overview of semantic image segmentation_.pdf
    │   ├── Article pool.md - Pool, from which we read articles.
    │   ├── Metal Additive Manufacturing Parts Inspection Using Convolutional Neural Network.pdf
    │   ├── Scratch Detection in Cars Using a Convolutional Neural Network by Means of Transfer Learning.pdf
    │   ├── useful - folder with useful articles
    │   ├── Useful.md - useful articles retold briefly
    │   ├── useless - folder with useless articles
    │   └── Useless.md - useless articles (To REMOVE)
    ├── code
    │   ├── README.md
    │   └── tools
    │       ├── filter - folder with filters
    │       ├── image.png - icon
    │       ├── image.py - image holder (for NumPy and PIL interpretation)
    │       ├── interface.py - interface script
    │       └── save.png - icon
    ├── datasets
    │   └── photos
    │       ├── annotations - Annotations created with LabelImg
    │       └── last.txt - Last reviewed image
    ├── docs
    │   └── README.md
    ├── here.jpg
    ├── LICENSE
    ├── localization.ipynb
    ├── README.md
    └── ssd_detector.ipynb

## Recommended Soft

<a name="recommend"/>

[Image annotation tool](https://github.com/tzutalin/labelImg) - for creating bounding boxes

<a name="thanks"/>

## Contributors

- [Max Prikhodko](https://github.com/max-prihodko) - AI developer, C++/Python developer
- [Polina Kozhukh](https://github.com/PolinaRise) - AI developer, C/C++ developer, GUI developer
- [Sergey Mirzoev](https://github.com/Mr-S-Mirzoev) - AI/CV developer, C/C++/Python developer, GUI/Core developer
