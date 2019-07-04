#!/bin/bash

echo 'Enter number for which experiment to conduct:'
echo '1) Delayed Conditioning        6) Simultaneous Conditioning'
echo '2) Second Order Conditioning   7) Compound Conditioning'
echo '3) Latent Inhibition           8) Sensory Preconditioning'
echo '4) Extinction                  9) Blocking'
echo '5) Partial Reinforcement      10) Extinction in Second Order Conditioning'

read expNum

# echo "run" | python3 scriptExp.py $(($expNum+10)) 1

for (( i=1; i<101; ++i )) ; do
	echo "run" | python3 scriptExp.py $(($expNum+10)) $i
done

# echo "run" | python3 scriptExp.py