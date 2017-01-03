# Ising Model

This is a simple implementation of 2 dimension Ising Model. The default parameters in Ising model are shown below
* J = 1
* B = 0
* k = 1
* Initial temperature = 1.5K
* Final   temperature = 3.5K

Feel free to change these values in metro.py.

### Run the program
If you want to run this program, you can download it through git clone or download the zipfile. Next, run the following command lines. Remind that don't just copy and paste these command lines, you have to change the lattice_col and lattice_row to the values which you can to see.

```sh
$ cd Ising_Model
$ python metro.py lattice_col lattice_row
```

The recommended values of lattice_col lattice_row is (100,100), which  perform best.
In every temperature, the program will run 2 million times of metropolis algorithm, so it really take times to run the program. If you want to save time, you can also change the iteration in every temperature to 200000, it can also perform similar results.