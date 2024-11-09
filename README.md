# 🎙️ Moroccan Darija TTS Project

This README gives an overview of the EDA done for the **Moroccan Darija TTS project**. It covers the main features of the dataset, including audio and text details, along with key sound features needed to train the TTS model.

## 📊 EDA Overview

### 1. **Dataset Overview**

- **📁 Total Audio Files:** `1006`  
  The dataset has **1006 recordings** of Moroccan Darija speech. Each file represents one sample, adding variety to help the TTS model learn different sounds in Darija.

- **⏱️ Average Duration:** `10.34` seconds  
  Each audio file is about **10.34 seconds long** on average, which meets our goal of 10–15 seconds per sample. This consistency helps create uniform segments for training.

- **🎶 Sample Rate:** `44100 Hz`  
  All recordings use a **44100 Hz sample rate** for clear, high-quality audio, making it easier to process for the TTS model.

![image](https://github.com/user-attachments/assets/04ffa20a-67f5-4a0d-8e40-85a612a7238e)

### 2. **📝 Text Analysis**

- **🔤 Total Characters:** `144,710`  
  The text data has **144,710 characters**, covering a wide range of vocabulary and sentence styles in Darija.

- **💬 Total Words:** `26,943`  
  There are **26,943 words** in total, giving enough variety to represent spoken Darija.

- **🌐 Total Arabic Words:** `25,904`  
  **25,904 words** are in Arabic, which is important for capturing Darija accurately.

- **🔍 Unique Words:** `6152`  
  The dataset includes **6152 unique words**, providing a broad vocabulary that helps the TTS model generalize across different terms and phrases.

![image](https://github.com/user-attachments/assets/01cd7ad9-efef-4e89-a17b-68aaa3a0a2c9)

### 3. **🔊 Acoustic Features**

The following acoustic features have been extracted from the audio files to provide additional input to the TTS model:

- **🎼 MFCC (Mel-Frequency Cepstral Coefficients):**  
  MFCC captures the unique sound patterns of speech, like how different letters and words sound. This helps the TTS model understand the basic building blocks of Darija pronunciation, making the generated speech clearer and more accurate.
![image](https://github.com/user-attachments/assets/3e9fed7f-598a-4c20-8257-012746514418)

- **🎵 Pitch Extraction:**  
  Pitch is the high or low sound of the voice. By capturing pitch, we can understand the natural rise and fall in the speaker's voice, which helps the TTS model sound more natural when replicating Darija speech.
![image](https://github.com/user-attachments/assets/aaeb99e4-10e6-4e3f-9c7b-59008e18bcce)

- **📈 Energy:**  
  Energy measures the loudness of each part of the audio. By understanding the volume changes, the TTS model can better mimic natural speech dynamics, making some parts sound louder or softer as in real conversations.
![image](https://github.com/user-attachments/assets/71ce5cc5-88e8-494c-9273-c6c16fa81b4f)

## 🎯 Purpose of EDA

The main goal of this EDA is to understand the **structure and details** of our dataset to help train the TTS model effectively. By studying both **text and sound features**, we can make sure the dataset is ready to produce **natural and clear Moroccan Darija speech**.

