#Se supone que no deberias estar aca pero bueno, si te entró la curiosidad o ves un error en el codigo y no sabes dodne esta

def test_perceptron_1(train_func):
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
    test_preds = [perceptron.predict(xi) for xi in X]

    #Asserts
    assert len(history["errors"]) == 20, "El historial debe tener 20 épocas."
    assert np.array_equal(test_results, y), f"Error: Se esperaba {y} pero se obtuvo {test_results}"

    print("Bien. El test ha pasado sin errores")

  except Exception as e:
    print(f"Falló el test:{e}")
    
