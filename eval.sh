for D in ./datasets/*
do
    currdir=$(basename $D)
    pref="./datasets/"
    echo "------ DATA SET: ${currdir} ---------------"
    #echo "NORMAL"
    #python ./code/classify.py --mode train --algorithm perceptron --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".train 
	#python ./code/classify.py --mode test --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".dev  --predictions-file "$pref$currdir/$currdir".predictions
	#python compute_accuracy.py "$pref$currdir/$currdir".dev "$pref$currdir/$currdir".predictions
    #echo "AVERAGE"
    #python ./code/classify.py --mode train --algorithm averaged_perceptron --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".train
	#python ./code/classify.py --mode test --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".dev  --predictions-file "$pref$currdir/$currdir".predictions
	#python compute_accuracy.py "$pref$currdir/$currdir".dev "$pref$currdir/$currdir".predictions
    #echo "MARGIN"
    #python ./code/classify.py --mode train --algorithm margin_perceptron --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".train
    #python ./code/classify.py --mode test --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".dev  --predictions-file "$pref$currdir/$currdir".predictions
    #python compute_accuracy.py "$pref$currdir/$currdir".dev "$pref$currdir/$currdir".predictions
    #echo "PEGASOS"
    #python ./code/classify.py --mode train --algorithm pegasos --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".train
    #python ./code/classify.py --mode test --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".dev  --predictions-file "$pref$currdir/$currdir".predictions
    #python compute_accuracy.py "$pref$currdir/$currdir".dev "$pref$currdir/$currdir".predictions
    #echo "STANDARD KNN"
    #python ./code/classify.py --mode train --algorithm knn --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".train
    #python ./code/classify.py --mode test --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".dev  --predictions-file "$pref$currdir/$currdir".predictions
    #python compute_accuracy.py "$pref$currdir/$currdir".dev "$pref$currdir/$currdir".predictions
    #echo "DISTANCE KNN"
    #python ./code/classify.py --mode train --algorithm distance_knn --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".train
    #python ./code/classify.py --mode test --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".dev  --predictions-file "$pref$currdir/$currdir".predictions
    #python compute_accuracy.py "$pref$currdir/$currdir".dev "$pref$currdir/$currdir".predictions
    echo "ADABOOST"
    python ./code/classify.py --mode train --algorithm adaboost --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".train
    python ./code/classify.py --mode test --model-file "$pref$currdir/$currdir".model --data "$pref$currdir/$currdir".dev  --predictions-file "$pref$currdir/$currdir".predictions
    python compute_accuracy.py "$pref$currdir/$currdir".dev "$pref$currdir/$currdir".predictions
done