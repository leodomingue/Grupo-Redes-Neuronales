#Se supone que no deberias estar aca pero bueno, si te entró la curiosidad o ves un error en el codigo y no sabes dodne esta

import numpy as np
def test_01_contructor_perceptron():
  try:
    test_perceptron = Perceptron(n_features=1)
    return True
  except:
    print("Test 1: No se pudo crear instancia de Perceptron")
    return False

def test_02_initialization_perceptron():
  try:
    test_perceptron = Perceptron(n_features=2)
    assert test_perceptron.weights is not None, "weights no inicializado"
    assert len(test_perceptron.weights) == 2, "weights no tiene dimensión correcta"
    assert test_perceptron.bias == 0.0, "bias no es 0.0"
    return True
  except AssertionError as e:
    print(f"Test 2: Error en constructor - {e}")
    return False

def test_03_step_function():
  test_perceptron = Perceptron(n_features=2)
  try:
    assert test_perceptron.step_function(1.0) == 1, "step_function(1.0) debería ser 1"
    assert test_perceptron.step_function(-1.0) == -1, "step_function(-1.0) debería ser -1"
    assert test_perceptron.step_function(0) == 1, "step_function(0) debería ser 1"
    return True
  except AssertionError as e:
      print(f"Test 3: Error en step_function - {e}")
      return False

def test_04_basic_predict():
  try:
    test_perceptron = Perceptron(n_features=2)
    test_perceptron.weights = np.array([1, 1])
    test_perceptron.bias = 0
    X_test = np.array([[1, 1], [-1, -1]])
    preds = test_perceptron.predict(X_test)
    assert len(preds) == 2, "predict no retorna array del tamaño correcto"
    return True
  except Exception as e:
      print(f"Test 4: Error en predict - {e}")
      return False

def test_05_AND_perceptron(train_perceptron):
  """
  Test AND
  """
  X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
  y = np.array([-1, -1, -1, 1])

  try:
    perceptron, history = train_perceptron(X, y, lr=0.1, epochs=20)

    test_preds = np.array([perceptron.predict(xi) for xi in X])

    assert history["errors"][-1] == 0, f"El perceptrón debería converger (0 errores), pero tiene {history['errors'][-1]} errores"
    assert perceptron.weights is not None, "Los pesos no fueron inicializados"
    assert perceptron.bias is not None, "El bias no fue inicializado"
    assert len(history["errors"]) == 20, f"El historial debe tener 20 épocas, tiene {len(history["errors"])}"
    assert len(history["weights"]) == 20, f"El historial de pesos debe tener 20 épocas, tiene {len(history["weights"])}"
    assert len(history["bias"]) == 20, f"El historial de biass debe tener 20 épocas, tiene {len(history["bias"])}"
    assert np.array_equal(test_preds, y), f"Error: Se esperaba {y} pero se obtuvo {test_preds}"
    assert perceptron.weights.shape == (X.shape[1],), f"Los pesos deben tener forma ({X.shape[1]},), tienen {perceptron.weights.shape}"
    return True

  except Exception as e:
    print(f"Test 5: Falló el test:{e}")

def test_06_OR_perceptron(train_perceptron):
  """
  Test OR
  """
  X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
  y = np.array([-1, 1, 1, 1])

  try:
    perceptron, history = train_perceptron(X, y, lr=0.1, epochs=30)

    test_preds = np.array([perceptron.predict(xi) for xi in X])

    assert history["errors"][-1] == 0, f"El perceptrón debería converger (0 errores), pero tiene {history['errors'][-1]} errores"
    assert perceptron.weights is not None, "Los pesos no fueron inicializados"
    assert perceptron.bias is not None, "El bias no fue inicializado"
    assert len(history["errors"]) == 30, f"El historial debe tener 30 épocas, tiene {len(history["errors"])}"
    assert len(history["weights"]) == 30, f"El historial de pesos debe tener 30 épocas, tiene {len(history["weights"])}"
    assert len(history["bias"]) == 30, f"El historial de biass debe tener 30 épocas, tiene {len(history["bias"])}"
    assert np.array_equal(test_preds, y), f"Error: Se esperaba {y} pero se obtuvo {test_preds}"
    assert perceptron.weights.shape == (X.shape[1],), f"Los pesos deben tener forma ({X.shape[1]},), tienen {perceptron.weights.shape}"
    return True

  except Exception as e:
    print(f"Test 6: Falló el test:{e}")

def run_all_tests_perceptron(train_perceptron):
  print("EJECUTANDO TODOS LOS TESTS")
  results = []

  results.append(test_01_contructor_perceptron())
  results.append(test_02_initialization_perceptron())
  results.append(test_03_step_function())
  results.append(test_04_basic_predict())
  results.append(test_05_AND_perceptron(train_perceptron))
  results.append(test_06_OR_perceptron(train_perceptron))

  all_passed = all(res is True for res in results)
  if all_passed:
    return True
    print("Todos los tests pasaron correctamente")
  else:
    print("Algunos tests fallaron")
    return False
