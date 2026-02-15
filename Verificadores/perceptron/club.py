import numpy as np

def test_accurracy_club(perceptron, x_original, y_original):

  try:
    X_mean_test = np.mean(x_original, axis=0)
    X_std_test = np.std(x_original, axis=0)
    X_scaled_test = (x_original - X_mean_test) / X_std_test

    predictions = perceptron.predict(X_scaled_test)
    accuracy = np.mean(predictions == y_original)

    if accuracy >= 0.90:
      print(f"Accuracy: {accuracy * 100:.2f}%")
      print("El test pasó")
      return True
    else:
      print(f"Accuracy insuficiente: {accuracy * 100:.2f}%")
      return False

  except Exception as e:
    print(f"Error: {e}")
