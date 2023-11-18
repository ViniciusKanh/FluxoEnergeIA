
from data_analysis import run_data_analysis
from preprocessing import preprocess_data
from model_training import train_model
from prediction import make_prediction

def main():
    # Carregar e analisar os dados
    df = run_data_analysis()

    # Pré-processar os dados
    X_train, X_test, y_train, y_test = preprocess_data(df)

    # Treinar o modelo
    model = train_model(X_train, y_train)

    # Fazer uma previsão
    resultado = make_prediction(model, X_test)
    print(f"Resultado da previsão: {resultado}")

if __name__ == "__main__":
    main()
