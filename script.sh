#/bin/bash
xx=1
x=1

for file in ./test/*.i386
do
    x=1
    for config in ./cfg/*.cfg
        do
        echo -e "caso: $file $x \n"
        m2s --x86-sim detailed --x86-max-inst 20000 --x86-config ./cfg/c4_$x.cfg --x86-report ./reports/report_$xx-$x.txt $file
        x=$((x+1))
        done
    xx=$((xx+1))
done


