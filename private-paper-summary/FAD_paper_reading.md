paper summarization

i only focus on the LA track of FAD

# icassp

## 2023

#### Learning From Yourself: A Self-Distillation Method for Fake Speech Detection

##### method

self-distillation, using deep layer to guide shallow layers feature and prediction result during training

[one final block guide the 3 former shallow blocks]

loss restriction including 

1. hard loss (using ground true label and final prediction), 
2. soft loss(using deep layer prediction and shallow layers prediction[adding additional classifiers]), 
3. feature loss (using L2 to compute final feature and the feature from the shallow layers)

##### experiments

proving points: this training methods can improve and gain competitive performance of base model (including ECANet9 ECANet18 ECANet34 ECANet50 SENet9 SENet18 SENet34 SENet50)

datasets: asvspoof19 LA+PA

not SOTA  but method is proved effective



#### Graph-Based Spectro-Temporal Dependency Modeling for Anti-Spoofing

##### method



##### experiments



#### Can Spoofing Countermeasure And Speaker Verification Systems Be Jointly Optimised?

##### method



##### experiments





#### An Antispoofing Approach in Biometric Authentication System for a Smartcard

##### method



##### experiments





#### Waveform Boundary Detection for Partially Spoofed Audio

##### method



##### experiments





#### Spoofed Training Data for Speech Spoofing Countermeasure Can Be Efficiently Created Using Neural Vocoders

##### method



##### experiments





#### Shift to Your Device: Data Augmentation for Device-Independent Speaker Verification Anti-Spoofing

##### method



##### experiments







#### SAMO: Speaker Attractor Multi-Center One-Class Learning For Voice Anti-Spoofing

##### method



##### experiments





#### Phase-Aware Spoof Speech Detection Based On Res2net with Phase Network

##### method



##### experiments





#### Leveraging Positional-Related Local-Global Dependency for Synthetic Speech Detection

##### method



##### experiments





#### Identifying Source Speakers for Voice Conversion Based Spoofing Attacks on Speaker Verification Systems

##### method



##### experiments







