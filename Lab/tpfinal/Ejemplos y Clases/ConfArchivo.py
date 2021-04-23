import argparse


parser = argparse.ArgumentParser()

#Parametro obligatorio y posicional
parser.add_argument("file name",help = "el nombre del grafo")

#parametro opcional
parser.add_argument("--verbosity","-v",help="incrementa el nivel de verbosidad de la ejecucion",action= "store_true")

args = parser.parse_args()

if args.verbosity:
    print("la verbosidad esta activada")

    
print("el nombre del archivo fue " + args.file_name)
