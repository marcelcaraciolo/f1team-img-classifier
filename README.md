# f1team-img-classifier
Classificador de Imagens para detecção de equipes de corrida de Fórmula 1 (Ano 2023) | Projeto CESAR SCHOOL DADOS 2023.1

## Projeto Final - Modelos Preditivos Conexionistas

### Marcel Pinheiro Caraciolo

|**Tipo de Projeto**|**Modelo Selecionado**|**Linguagem**|
|--|--|--|
|Classificação de Imagens|ex.: EfficientNetB0| Tensorflow|

## Performance

O modelo treinado possui performance de acurácia de testes de 84.05% e  loss na base de testes de 0.4204*.

### Output do bloco de treinamento

<details>
  <summary>Click to expand!</summary>
  
  ```text
wandb: WARNING The save_model argument by default saves the model in the HDF5 format that cannot save custom objects like subclassed models and custom layers. This behavior will be deprecated in a future release in favor of the SavedModel format. Meanwhile, the HDF5 model is saved as W&B files and the SavedModel as W&B Artifacts.
Epoch 1/5
61/61 [==============================] - ETA: 0s - loss: 1.9079 - accuracy: 0.3770
Epoch 1: val_loss improved from inf to 1.73944, saving model to ./ModelCheckPoints/model_1.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 48s 548ms/step - loss: 1.9079 - accuracy: 0.3770 - val_loss: 1.7394 - val_accuracy: 0.4417
Epoch 2/5
60/61 [============================>.] - ETA: 0s - loss: 1.2348 - accuracy: 0.7375
Epoch 2: val_loss improved from 1.73944 to 1.37097, saving model to ./ModelCheckPoints/model_1.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 31s 514ms/step - loss: 1.2335 - accuracy: 0.7375 - val_loss: 1.3710 - val_accuracy: 0.6074
Epoch 3/5
61/61 [==============================] - ETA: 0s - loss: 0.9023 - accuracy: 0.8444
Epoch 3: val_loss improved from 1.37097 to 1.19029, saving model to ./ModelCheckPoints/model_1.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 33s 537ms/step - loss: 0.9023 - accuracy: 0.8444 - val_loss: 1.1903 - val_accuracy: 0.6626
Epoch 4/5
60/61 [============================>.] - ETA: 0s - loss: 0.7061 - accuracy: 0.9047
Epoch 4: val_loss improved from 1.19029 to 1.05559, saving model to ./ModelCheckPoints/model_1.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 33s 545ms/step - loss: 0.7055 - accuracy: 0.9045 - val_loss: 1.0556 - val_accuracy: 0.7178
Epoch 5/5
60/61 [============================>.] - ETA: 0s - loss: 0.5759 - accuracy: 0.9312
Epoch 5: val_loss improved from 1.05559 to 0.98177, saving model to ./ModelCheckPoints/model_1.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 32s 529ms/step - loss: 0.5745 - accuracy: 0.9312 - val_loss: 0.9818 - val_accuracy: 0.7362


Epoch 5/30
61/61 [==============================] - ETA: 0s - loss: 0.3025 - accuracy: 0.9404
Epoch 5: val_loss improved from inf to 0.58905, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 52s 570ms/step - loss: 0.3025 - accuracy: 0.9404 - val_loss: 0.5890 - val_accuracy: 0.8160 - lr: 1.0000e-04
Epoch 6/30
60/61 [============================>.] - ETA: 0s - loss: 0.1323 - accuracy: 0.9766
Epoch 6: val_loss improved from 0.58905 to 0.49953, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 33s 551ms/step - loss: 0.1314 - accuracy: 0.9769 - val_loss: 0.4995 - val_accuracy: 0.8098 - lr: 1.0000e-04
Epoch 7/30
60/61 [============================>.] - ETA: 0s - loss: 0.0764 - accuracy: 0.9922
Epoch 7: val_loss improved from 0.49953 to 0.48511, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 32s 526ms/step - loss: 0.0761 - accuracy: 0.9923 - val_loss: 0.4851 - val_accuracy: 0.8405 - lr: 1.0000e-04
Epoch 8/30
60/61 [============================>.] - ETA: 0s - loss: 0.0463 - accuracy: 0.9979
Epoch 8: val_loss improved from 0.48511 to 0.44143, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 33s 545ms/step - loss: 0.0462 - accuracy: 0.9979 - val_loss: 0.4414 - val_accuracy: 0.8405 - lr: 1.0000e-04
Epoch 9/30
60/61 [============================>.] - ETA: 0s - loss: 0.0323 - accuracy: 0.9995
Epoch 9: val_loss improved from 0.44143 to 0.43880, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 33s 542ms/step - loss: 0.0321 - accuracy: 0.9995 - val_loss: 0.4388 - val_accuracy: 0.8466 - lr: 1.0000e-04
Epoch 10/30
60/61 [============================>.] - ETA: 0s - loss: 0.0220 - accuracy: 1.0000
Epoch 10: val_loss did not improve from 0.43880
61/61 [==============================] - 4s 57ms/step - loss: 0.0220 - accuracy: 1.0000 - val_loss: 0.4441 - val_accuracy: 0.8466 - lr: 1.0000e-04
Epoch 11/30
60/61 [============================>.] - ETA: 0s - loss: 0.0158 - accuracy: 1.0000
Epoch 11: val_loss improved from 0.43880 to 0.42839, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.2s
61/61 [==============================] - 31s 521ms/step - loss: 0.0158 - accuracy: 1.0000 - val_loss: 0.4284 - val_accuracy: 0.8405 - lr: 1.0000e-04
Epoch 12/30
60/61 [============================>.] - ETA: 0s - loss: 0.0123 - accuracy: 1.0000
Epoch 12: val_loss improved from 0.42839 to 0.42563, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 32s 529ms/step - loss: 0.0123 - accuracy: 1.0000 - val_loss: 0.4256 - val_accuracy: 0.8466 - lr: 1.0000e-04
Epoch 13/30
60/61 [============================>.] - ETA: 0s - loss: 0.0099 - accuracy: 1.0000
Epoch 13: val_loss improved from 0.42563 to 0.42320, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 32s 522ms/step - loss: 0.0099 - accuracy: 1.0000 - val_loss: 0.4232 - val_accuracy: 0.8405 - lr: 1.0000e-04
Epoch 14/30
60/61 [============================>.] - ETA: 0s - loss: 0.0080 - accuracy: 1.0000
Epoch 14: val_loss did not improve from 0.42320
61/61 [==============================] - 4s 57ms/step - loss: 0.0080 - accuracy: 1.0000 - val_loss: 0.4244 - val_accuracy: 0.8466 - lr: 1.0000e-04
Epoch 15/30
61/61 [==============================] - ETA: 0s - loss: 0.0067 - accuracy: 1.0000
Epoch 15: val_loss did not improve from 0.42320
61/61 [==============================] - 3s 51ms/step - loss: 0.0067 - accuracy: 1.0000 - val_loss: 0.4265 - val_accuracy: 0.8466 - lr: 1.0000e-04
Epoch 16/30
60/61 [============================>.] - ETA: 0s - loss: 0.0056 - accuracy: 1.0000
Epoch 16: val_loss did not improve from 0.42320

Epoch 16: ReduceLROnPlateau reducing learning rate to 1.9999999494757503e-05.
61/61 [==============================] - 4s 59ms/step - loss: 0.0056 - accuracy: 1.0000 - val_loss: 0.4267 - val_accuracy: 0.8405 - lr: 1.0000e-04
Epoch 17/30
61/61 [==============================] - ETA: 0s - loss: 0.0049 - accuracy: 1.0000
Epoch 17: val_loss improved from 0.42320 to 0.42114, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 32s 525ms/step - loss: 0.0049 - accuracy: 1.0000 - val_loss: 0.4211 - val_accuracy: 0.8405 - lr: 2.0000e-05
Epoch 18/30
60/61 [============================>.] - ETA: 0s - loss: 0.0046 - accuracy: 1.0000
Epoch 18: val_loss improved from 0.42114 to 0.42105, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 32s 535ms/step - loss: 0.0046 - accuracy: 1.0000 - val_loss: 0.4210 - val_accuracy: 0.8466 - lr: 2.0000e-05
Epoch 19/30
61/61 [==============================] - ETA: 0s - loss: 0.0044 - accuracy: 1.0000
Epoch 19: val_loss improved from 0.42105 to 0.42061, saving model to ./ModelCheckPoints/model_2.ckpt
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 33s 537ms/step - loss: 0.0044 - accuracy: 1.0000 - val_loss: 0.4206 - val_accuracy: 0.8405 - lr: 2.0000e-05
Epoch 20/30
60/61 [============================>.] - ETA: 0s - loss: 0.0044 - accuracy: 1.0000
Epoch 20: val_loss improved from 0.42061 to 0.42042, saving model to ./ModelCheckPoints/model_2.ckpt

Epoch 20: ReduceLROnPlateau reducing learning rate to 3.999999898951501e-06.
/usr/local/lib/python3.10/dist-packages/keras/src/engine/training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
wandb: Adding directory to artifact (/content/wandb/run-20231021_174156-buuhazik/files/model-best)... Done. 0.1s
61/61 [==============================] - 32s 524ms/step - loss: 0.0043 - accuracy: 1.0000 - val_loss: 0.4204 - val_accuracy: 0.8405 - lr: 2.0000e-05
Epoch 21/30
60/61 [============================>.] - ETA: 0s - loss: 0.0041 - accuracy: 1.0000
Epoch 21: val_loss did not improve from 0.42042
61/61 [==============================] - 3s 52ms/step - loss: 0.0042 - accuracy: 1.0000 - val_loss: 0.4216 - val_accuracy: 0.8405 - lr: 4.0000e-06
Epoch 22/30
60/61 [============================>.] - ETA: 0s - loss: 0.0041 - accuracy: 1.0000
Epoch 22: val_loss did not improve from 0.42042
61/61 [==============================] - 3s 53ms/step - loss: 0.0041 - accuracy: 1.0000 - val_loss: 0.4216 - val_accuracy: 0.8466 - lr: 4.0000e-06
Epoch 23/30
61/61 [==============================] - ETA: 0s - loss: 0.0041 - accuracy: 1.0000
Epoch 23: val_loss did not improve from 0.42042

Epoch 23: ReduceLROnPlateau reducing learning rate to 7.999999979801942e-07.
61/61 [==============================] - 4s 57ms/step - loss: 0.0041 - accuracy: 1.0000 - val_loss: 0.4213 - val_accuracy: 0.8466 - lr: 4.0000e-06
Epoch 24/30
61/61 [==============================] - ETA: 0s - loss: 0.0040 - accuracy: 1.0000
Epoch 24: val_loss did not improve from 0.42042
61/61 [==============================] - 3s 50ms/step - loss: 0.0040 - accuracy: 1.0000 - val_loss: 0.4214 - val_accuracy: 0.8466 - lr: 8.0000e-07
Epoch 25/30
61/61 [==============================] - ETA: 0s - loss: 0.0040 - accuracy: 1.0000
Epoch 25: val_loss did not improve from 0.42042
Restoring model weights from the end of the best epoch: 20.
61/61 [==============================] - 3s 53ms/step - loss: 0.0040 - accuracy: 1.0000 - val_loss: 0.4214 - val_accuracy: 0.8466 - lr: 8.0000e-07
Epoch 25: early stopping
  ```
</details>


### Evidências do treinamento

Nessa seção você deve colocar qualquer evidência do treinamento, como por exemplo gráficos de perda, performance, matriz de confusão etc.

![WANDB](https://api.wandb.ai/links/marcelcaraciolo/bv9u8tuk)



Exemplo de adição de imagem:
![Descrição](https://picsum.photos/seed/picsum/500/300)

## Roboflow

Nessa seção deve colocar o link para acessar o dataset no Roboflow

Exemplo de link: [F1 Car Teams](https://universe.roboflow.com/corriporai/f1-car-teams)

## HuggingFace

Nessa seção você deve publicar o link para o HuggingFace
