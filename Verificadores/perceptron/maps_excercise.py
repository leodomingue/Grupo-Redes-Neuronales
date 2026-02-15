import numpy as np
from sklearn.datasets import make_classification

def test_01_first_map(perceptron):
  X_test, y_test = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, n_classes=2,n_clusters_per_class=1,
                           flip_y=0, class_sep=2.0, random_state=11)
  y_test = np.where(y_test == 0, -1, 1)
  try:
    assert len(perceptron.weights) == 2, f"Los pesos deberían tener 2 dimensiones, tienen {len(perceptron.weights)}"
    predictions = perceptron.predict(X_test)
    accuracy = np.mean(predictions == y_test)
    if accuracy == 1.0:
      return True
    else:
      print(f"Accuracy insuficiente: {accuracy * 100:.2f}%")
      print(" Este dataset es linealmente separable. Deberías alcanzar 100%")
      print("Deberias aumentar las epocas y asegurarte de usar lr = 0.01")
      return False
  except Exception as e:
      print(f" Error calculando accuracy - {e}")
      return False

def test_02_second_map(perceptron):
  X_test, y_test = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, n_classes=2,n_clusters_per_class=1,
                           flip_y=0, class_sep=3.0, random_state=12)
  y_test = np.where(y_test == 0, -1, 1)
  try:
    assert len(perceptron.weights) == 2, f"Los pesos deberían tener 2 dimensiones, tienen {len(perceptron.weights)}"
    predictions = perceptron.predict(X_test)
    accuracy = np.mean(predictions == y_test)
    if accuracy == 1.0:
      return True
    else:
      print(f"Accuracy insuficiente: {accuracy * 100:.2f}%")
      print(" Este dataset es linealmente separable. Deberías alcanzar 100%")
      print("Deberias aumentar las epocas y asegurarte de usar lr = 0.01")
      return False
  except Exception as e:
      print(f"Error calculando accuracy - {e}")
      return False

def run_all_tests_exercise_1(first_perceptron, second_perceptron):
  print("EJECUTANDO TODOS LOS TESTS")
  results = []

  results.append(test_01_first_map(first_perceptron))
  results.append(test_02_second_map(second_perceptron))

  all_passed = all(res is True for res in results)
  if all_passed:
    print("Todos los tests pasaron correctamente")
    return True
  else:
    print("Algunos tests fallaron")
    return False
