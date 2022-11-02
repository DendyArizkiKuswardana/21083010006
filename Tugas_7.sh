#/bin/bash

unsur() {
    parameter1=$1
    parameter2=$2
    parameter3=$3
    echo "nilai dari panjang: $parameter1"
    echo "nilai dari lebar: $parameter2"
    echo "nilai dari luas persegi panjang: "
    expr $parameter1 \* $parameter2
}

echo "masukkan panjang: "
read a
echo "masukkan lebar: "
read b
echo "luas persegi panjang: "
expr $a \* $b

printf "\n"
unsur $a $b $c
