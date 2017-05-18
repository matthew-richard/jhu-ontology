for D in ./datasets/*
do
    currdir=$(basename $D)
    pref="./datasets/"
    echo "------ DATA SET: ${currdir} ---------------"
    echo "LOCATION"
    python ./code/load_data.py --mode train --algorithm location --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".train 
	python ./code/load_data.py --mode test --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".dev  --predictions-file "$pref$currdir/$currdir".predictions
	python compute_accuracy.py "$pref$currdir/$currdir".dev "$pref$currdir/$currdir".predictions
    #echo "BUILDING"
    #python ./code/load_data.py --mode train --algorithm building --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".train
    #python ./code/load_data.py --mode test --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".dev  --predictions-file "$pref$currdir/$currdir".predictions
    #python compute_accuracy.py "$pref$currdir/$currdir".dev "$pref$currdir/$currdir".predictions
done