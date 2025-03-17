import hmmlearn as hmm
from hmmlearn.hmm import GaussianHMM
import numpy as np
from preprocessing import preprocessing_data 
from data_loader import fetch_stock_data


def train_hmm(data):
    """
        Trains the Hidden Markov Model(HMMs) to generate the possible sequence of hidden states 
        using the EM Algorithm(Baum-Welch Algorithm (a special case of EM for HMMs)).For stock data there are three possible hidden states possibles
        (Bull, Bear and Neutral Market)

        Args:
            -data:DataFrame consisting of stock data.
        Returns:
            - The possible sequence for possible hidden states.
    
    """
    np.random.seed(42)
    log_returns=preprocessing_data(data)

    ## Initializing the hidden markov model 

    hmm=GaussianHMM(n_components=3,covariance_type="full",n_iter=400,random_state=42)

    ## Fitting the model into data 

    hmm.fit(log_returns)

    ## Predicting the possible hidden state 

    hidden_states=hmm.predict(log_returns)

    return hmm,hidden_states

def hmm_parameters(hmm):
    """
        Prints the Parameters of hidden Markov Models. A Hidden Markov Model can be completely identified using 3 sets of parameters.
            -Initial State Probabilities (π)
            -Transition Probability Matrix (A) 
            -Emission Probability (Gaussian in this case)

        Args:
            -hmm: HMMs Model with defined parameters.

        Returns:
            -Print the Parameters of hidden Markov Models.
    
    """
    print("\n🔹 Mean Log Returns for Each State:")
    print(hmm.means_)  # Mean log returns for each state

    print("\n🔹 Covariances of Each State:")
    print(hmm.covars_)  # Covariance matrix for each hidden state

    print("\n🔹 Transition Probability Matrix:")
    print(hmm.transmat_)  # Probability of moving from one state to another

    print("\n🔹 Initial State Probabilities (π):")
    print(hmm.startprob_)  # Probability of starting in each state

