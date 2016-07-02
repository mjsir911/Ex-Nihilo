# Ex-Nihilo

**Ex Nihilo** is an open source software library for procedurally generating star systems and the planets inside using randomly generated seeds or a user-defined seed. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

To run the scripts, [Blender](www.blender.org) has to be installed and working properly. Extremely minimal knowledge in blender is required to get scripts up and running.

### Installing

To procure a running developmental environment, clone the latest stable branch from the git repository.

Once the git repository has been cloned and located, and blender has been installed, you must run blender to automatically run a python file ([launchblend.py](src/launchblend.py)). This is typically done with the blender command, but depending on your software may be subject to change

```
blender -P /path/to/repo/src/launchblend.py /path/to/repo/standard.blend
```

And now depending on how in depth you want to use these libraries, you can either run the script directly from the blender text editor or import the entire package and work from there inside the built in interactive terminal

If you want to generate everything from the text editor, just change the optional settings in the text file open up on the screen called "startup" and press "run script" to the right of the file name. The generation may take a while, blender did **not** crash if it is frozen up

If you want to experiment around with the package, just import the package through the interactive terminal, the git repository was already added to the path on startup

```
import src
```

After the instructions above have been followed, blender will freeze up for a time depending on the randomly generated seed due to a large amount of computations. After the computations have been made the objects have been generated and one will see the generated objects on the 3D portion of the screen

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* Dropwizard - Bla bla bla
* Maven - Maybe
* Atom - ergaerga

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

