import EdgePrediction as ep
inst = ep.EdgePrediction()
print("Successfully loaded EdgePrediction !")
# TODO: Look at the CSV_to_graph approach
# TODO: How is the graph being constructed ?
inst.CSV_to_graph('data/data.csv', header=True, srcNameCol=0, srcTypeCol=1, tgtNameCol=4, tgtTypeCol=3, edgeTypeCol=2)
inst.preprocess()
inst.to_predict = 'HAS_SIDE_EFFECT'
inst.network_order = ['HAS_SIDE_EFFECT', 'DRUG_TARGETS', 'INDICATED_FOR']

result = inst.predict(target='C0027849', calculate_auc=True)

results = inst.predictAll(calculate_auc=True)
"""
Alternatively you can load the results in the following way:
"""
import json
results_from_json = json.load(open('/vagrant/results.json'))
result_from_json = json.load(open('/vagrant/result.json'))


"""
Successfully loaded EdgePrediction !
524 source nodes are common to all 3 input graphs
deleting 6116 nodes that don't overlap between networks
deleting another 3347 nodes that now have degree zero
deleting 79 nodes that don't overlap between networks
deleting another 80 nodes that now have degree zero
deleting 95 nodes that don't overlap between networks
deleting another 121 nodes that now have degree zero
ignoring C0027849 as a predictor in network HAS_SIDE_EFFECT

"""
