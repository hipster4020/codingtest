import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Bidirectional


def create_data():
    # # RNN의 입력 형태는 3D Tensor
    train_X = [[[0.1, 4.2, 1.5, 1.1, 2.8], [1.0, 3.1, 2.5, 0.7, 1.1], [0.3, 2.1, 1.5, 2.1, 0.1], [2.2, 1.4, 0.5, 0.9, 1.1]]]
    train_X = np.array(train_X).astype(np.float32)
    
    print(np.shape(train_X))
    print("         ")
    print(train_X)
    
    return train_X

def main(train_data):
    # return_state가 True면 마지막 시점 은닉 상태, 마지막 시점 은닉 상태, 셀 상태 반환
    lstm = LSTM(3, return_sequences=False, return_state=True)
    hidden_state, last_state, last_cell_state = lstm(train_X)
    
    print("return_state True, return_sequences False 마지막 시점 은닉 상태, 마지막 시점 은닉 상태, 셀 상태 반환")
    print('hidden state : {}, shape: {}'.format(hidden_state, hidden_state.shape))
    print('last hidden state : {}, shape: {}'.format(last_state, last_state.shape))
    print('last cell state : {}, shape: {}'.format(last_cell_state, last_cell_state.shape))
    print("---------------------------------------------------------------------------------")
    
    # return_sequences, return_state가 True면 모든 시점 은닉 상태, 마지막 시점 은닉 상태, 셀 상태 반환
    lstm = LSTM(3, return_sequences=True, return_state=True)
    hidden_states, last_hidden_state, last_cell_state = lstm(train_X)

    print("return_state, return_sequences True 마지막 시점 은닉 상태, 마지막 시점 은닉 상태, 셀 상태 반환")
    print('hidden states : {}, shape: {}'.format(hidden_states, hidden_states.shape))
    print('last hidden state : {}, shape: {}'.format(last_hidden_state, last_hidden_state.shape))
    print('last cell state : {}, shape: {}'.format(last_cell_state, last_cell_state.shape))

    
if __name__ == "__main__":
    train_X = create_data()
    main(train_X)