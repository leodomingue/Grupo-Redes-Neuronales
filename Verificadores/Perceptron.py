#Se supone que no deberias estar aca pero bueno, si te entró la curiosidad o ves un error en el codigo y no sabes dodne esta

import numpy as np

def test_perceptron_1(train_perceptron):
  """
  Test AND
  """

  #Input
  X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
  y = np.array([-1, -1, -1, 1])

  #Verificator
  try:
    #Execute fit
    perceptron, history = train_perceptron(X, y, lr=0.1, epochs=20)

    #Get predictions
    test_preds = np.array([perceptron.predict(xi) for xi in X])

    #Asserts
    assert history["errors"][-1] == 0, f"El perceptrón debería converger (0 errores), pero tiene {history['errors'][-1]} errores"
    assert perceptron.weights is not None, "Los pesos no fueron inicializados"
    assert perceptron.bias is not None, "El bias no fue inicializado"
    assert len(history["errors"]) == 20, f"El historial debe tener 20 épocas, tiene {len(history["errors"])}"
    assert len(history["weights"]) == 20, f"El historial de pesos debe tener 20 épocas, tiene {len(history["weights"])}"
    assert len(history["bias"]) == 20, f"El historial de biass debe tener 20 épocas, tiene {len(history["bias"])}"
    assert np.array_equal(test_preds, y), f"Error: Se esperaba {y} pero se obtuvo {test_preds}"
    assert perceptron.weights.shape == (X.shape[1],), f"Los pesos deben tener forma ({X.shape[1]},), tienen {perceptron.weights.shape}"

    print("Bien. El test ha pasado sin errores")

  except Exception as e:
    print(f"Falló el test:{e}")


def test_perceptron_2(train_perceptron):
  """
  Test OR
  """

  #Input
  X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
  y = np.array([-1, 1, 1, 1])

  #Verificator
  try:
    #Execute fit
    perceptron, history = train_perceptron(X, y, lr=0.1, epochs=30)

    #Get predictions
    test_preds = np.array([perceptron.predict(xi) for xi in X])

    #Asserts
    assert history["errors"][-1] == 0, f"El perceptrón debería converger (0 errores), pero tiene {history['errors'][-1]} errores"
    assert perceptron.weights is not None, "Los pesos no fueron inicializados"
    assert perceptron.bias is not None, "El bias no fue inicializado"
    assert len(history["errors"]) == 30, f"El historial debe tener 30 épocas, tiene {len(history["errors"])}"
    assert len(history["weights"]) == 30, f"El historial de pesos debe tener 30 épocas, tiene {len(history["weights"])}"
    assert len(history["bias"]) == 30, f"El historial de biass debe tener 30 épocas, tiene {len(history["bias"])}"
    assert np.array_equal(test_preds, y), f"Error: Se esperaba {y} pero se obtuvo {test_preds}"
    assert perceptron.weights.shape == (X.shape[1],), f"Los pesos deben tener forma ({X.shape[1]},), tienen {perceptron.weights.shape}"

    print("Bien. El test ha pasado sin errores")

  except Exception as e:
    print(f"Falló el test:{e}")


def run_all_tests(train_perceptron):
    """
    Run all tests for the perceptron.
    """
    print("EJECUTANDO TODOS LOS TESTS")
    
    print("\n1. Test 1:")
    test_perceptron_1(train_perceptron)
    
    print("\n2. Test 2:")
    test_perceptron_2(train_perceptron)
    
