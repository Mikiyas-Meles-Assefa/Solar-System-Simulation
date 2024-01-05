# Solar System Simulation

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

## Overview

The Solar System Simulation project is an interactive program that simulates the orbits of planets and celestial bodies within our Solar System. It provides a visual representation of planetary motion and gravitational forces, making it an educational and captivating tool for space enthusiasts and learners.

##Why I build it
I started to build this after I learned about gravitational motion in my junior year, and I wanted to check if we calculate the forces between each planet and other masses in that system result in an acceleration and hence change in velocity to create an elliptical path and my program verified that it it is true.

![Solar System Simulation Screenshot](mySolar_System/image.png)

## How to Run

To run the Solar System Simulation on your local machine, follow these steps:

1. **Prerequisites**: Ensure you have Python and Fortran installed on your system.

2. **Clone the Repository**: Clone this GitHub repository to your local machine using the following command:

   ```bash
   git clone https://github.com/Mikiyas-Meles-Assefa/Solar-System-Simulation.git
   ```

3. **Navigate to the Project Directory**: Change your current directory to the project folder:

   ```bash
   cd Solar-System-Simulation
   ```

4. **Compile and Execute**: Compile the Fortran code and run the Python front-end by executing the following command:

   ```bash
   ./run_simulation.sh
   ```

   This script will compile the Fortran code and then execute the Python program with Pygame to visualize the Solar System simulation.

## Documentation

The Solar System Simulation project is implemented in Fortran and Python. The Fortran code handles the backend calculations, while the Python code, along with Pygame, creates the interactive front end.

The simulation uses Newton's law of universal gravitation to calculate the gravitational forces between celestial bodies, resulting in realistic planetary orbits.

## License

This project is open-source and available under the [MIT License](LICENSE.md). You are free to use, modify, and distribute this code as long as you adhere to the terms of the license.

## Acknowledgments

This project was made possible with the contributions of open-source libraries and resources from the scientific and programming communities. I would like to acknowledge the [Pygame] (https://www.pygame.org/) community for their invaluable contributions to this project. Pygame library provided the foundation for creating the interactive front end of the Solar System simulation.

- Pygame: [https://www.pygame.org/](https://www.pygame.org/)


## Contact
For questions, suggestions, or contributions, please feel free to contact the project maintainer:

- Mikiyas Meles Assefa
- Email: mikiyasmeles.302419.cs@gmail.com
- GitHub: [https://github.com/Mikiyas-Meles-Assefa)

## Contributing

If you would like to contribute to this project, I welcome contributions from the community. 

## Updates and Maintenance

This project is actively maintained, and updates are planned to enhance its features and usability. Community contributions and feedback are highly appreciated in the ongoing development of the Solar System Simulation.
