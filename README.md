# Awesome-fake-audio-detection![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

A list of tools, papers and code related to Fake Audio Detection.. 

If you want to contribute to this list, welcome to send me a pull request or contact me :) 

This repo only collect papers related to FAD.  

Here is nothing about speech signal processing, speech synthesis, Speech Enhancement, data augmentation, voice conversion and speech edition. But learning them is beneficial to your research about FAD.

## Contents

- [Datasets](#datasets)
- [Competitions](#competitions)
- [Tools](#tools)
- [Recent Conference Papers](#recent-conference-papers)
- [different category](#category)
- [enlightening](#enlightening)




# datasets

- **ASVspoof2015-2017-2019-2021:** [website](https://www.asvspoof.org/database )
- **partial spoof**: [paper](https://arxiv.org/pdf/2204.05177.pdf) [dataset download](https://zenodo.org/record/5766198)
- **wavefake**:  [paper](https://arxiv.org/pdf/2111.02813.pdf)  [dataset download](https://zenodo.org/record/5642694#:~:text=WaveFake%3A%20A%20data%20set%20to%20facilitate%20audio%20DeepFake,finding%20new%20detection%20methods%20to%20prevent%20such%20attempts.) 
- **In-the-Wild:**  [website](https://deepfake-demo.aisec.fraunhofer.de/in_the_wild)  [paper](https://arxiv.org/pdf/2203.16263.pdf)  [dataset download](https://owncloud.fraunhofer.de/index.php/s/JZgXh0JEAF0elxa)
- **APTLY** [website](https://bil.eecs.yorku.ca/datasets/)




# competitions

- **ASVspoof:** https://www.asvspoof.org/



# tools

[asvspoof2021 baseline implementation](https://github.com/asvspoof-challenge/2021.git)



# recent conference papers

## interspeech [website](https://interspeech2023.org/)

### 2023 [papers](https://www.isca-speech.org/archive/interspeech_2023/)

- Robust Audio Anti-Spoofing with Fusion-Reconstruction Learning on Multi-Order Spectrograms [paper](https://www.isca-speech.org/archive/interspeech_2023/wen23_interspeech.html)
- Malafide: a novel adversarial convolutive noise attack against deepfake and spoofing detection systems [paper](https://www.isca-speech.org/archive/interspeech_2023/panariello23b_interspeech.html)
- How to Construct Perfect and Worse-than-Coin-Flip Spoofing Countermeasures: A Word of Warning on Shortcut Learning [paper](https://www.isca-speech.org/archive/interspeech_2023/shim23b_interspeech.html)
- Spoofing Attacker Also Benefits from Self-Supervised Pretrained Model [paper](https://www.isca-speech.org/archive/interspeech_2023/ito23_interspeech.html)
- Towards single integrated spoofing-aware speaker verification embeddings [paper](https://www.isca-speech.org/archive/interspeech_2023/mun23_interspeech.html)
- DoubleDeceiver: Deceiving the Speaker Verification System Protected by Spoofing Countermeasures [paper](https://www.isca-speech.org/archive/interspeech_2023/zhang23c_interspeech.html)
- Speaker-Aware Anti-spoofing [paper](https://www.isca-speech.org/archive/interspeech_2023/liu23o_interspeech.html)
- Range-Based Equal Error Rate for Spoof Localization [paper](https://www.isca-speech.org/archive/interspeech_2023/zhang23v_interspeech.html)
- A conformer-based classifier for variable-length utterance processing in anti-spoofing [paper](https://www.isca-speech.org/archive/interspeech_2023/rosello23_interspeech.html)
- Multi-Dataset Co-Training with Sharpness-Aware Optimization for Audio Anti-spoofing [paper](https://www.isca-speech.org/archive/interspeech_2023/shim23c_interspeech.html)
- Phase perturbation improves channel robustness for speech spoofing countermeasures [paper](https://www.isca-speech.org/archive/interspeech_2023/zang23_interspeech.html)
- Towards Attention-based Contrastive Learning for Audio Spoof Detection [paper](https://www.isca-speech.org/archive/interspeech_2023/goel23_interspeech.html)
- Synthetic Voice Spoofing Detection based on Feature Pyramid Conformer [paper](https://www.isca-speech.org/archive/interspeech_2023/gong23b_interspeech.html)
- Robust audio anti-spoofing countermeasure with joint training of front-end and back-end models [paper](https://www.isca-speech.org/archive/interspeech_2023/wang23v_interspeech.html#:~:text=Therefore%2C%20we%20proposes%20a%20new%20framework%20for%20robust,framework%20is%20more%20effective%20than%20the%20cascaded%20framework.)





## ICASSP [website](https://2023.ieeeicassp.org/)

### 2024 (submitted but not accepted yet)
- Can large-scale vocoded spoofed data improve speech spoofing countermeasure with a self-supervised front end? [paper](https://arxiv.org/pdf/2309.06014.pdf)
- Towards generalisable and calibrated synthetic speech detection with self-supervised representations [paper](https://arxiv.org/abs/2309.05384)

### 2023

- Learning From Yourself: A Self-Distillation Method for Fake Speech Detection [paper](https://arxiv.org/pdf/2303.01211.pdf) 
- Can spoofing countermeasure and speaker verification systems be jointly optimised?? [paper](https://arxiv.org/pdf/2303.07073.pdf)
- Spoofed training data for speech spoofing countermeasure can be efficiently created using neural vocoders  [paper](https://arxiv.org/pdf/2210.10570.pdf)
- Phase-Aware Spoof Speech Detection Based on Res2Net with Phase Network [paper](https://arxiv.org/pdf/2203.10793.pdf)
- Leveraging Positional-Related Local-Global Dependency for Synthetic Speech Detection [paper](https://ieeexplore.ieee.org/document/10096278)
- Reliability Estimation for Synthetic Speech Detection [paper](https://ieeexplore.ieee.org/abstract/document/10095524)








## SPL [website](https://dblp.uni-trier.de/db/journals/spl/index.html)

### 2023

- End-to-End Dual-Branch Network Towards Synthetic Speech Detection [paper](https://ieeexplore.ieee.org/document/10082951) [code](https://github.com/makaijie/End-to-End-Dual-Branch-Network-Towards-Synthetic-Speech-Detection)





# category

## model

### graph neural network	

- Aasist: Audio anti-spoofing using integrated spectro-temporal graph attention networks [paper](https://arxiv.org/pdf/2110.01200.pdf) [code](https://github.com/clovaai/aasist) 
- End-to-End Spectro-Temporal Graph Attention Networks for Speaker Verification Anti-Spoofing and Speech Deepfake Detection [paper](https://arxiv.org/pdf/2107.12710.pdf)  [code](https://github.com/eurecom-asp/RawGAT-ST-antispoofing)

### CQCC feature

- Constant Q Cepstral Coefficients: A Spoofing Countermeasure for Automatic Speaker Verification [paper](https://www.asvspoof.org/papers/CSL_CQCC.pdf)  [code is implemented in the asvspoof baselines]
- Towards End-to-End Synthetic Speech Detection [paper](https://arxiv.org/pdf/2106.06341.pdf) 

### sincnet&rawnet

- SPEAKER RECOGNITION FROM RAW WAVEFORM WITH SINCNET [paper](https://arxiv.org/pdf/1808.00158.pdf) [code](https://github.com/mravanelli/SincNet/)

  rawnet 	[1、2、3 all code](https://github.com/Jungjee/RawNet) 

- RawNet: Advanced end-to-end deep neural network using raw waveforms for text-independent speaker verification [paper](https://arxiv.org/pdf/1904.08104.pdf) 

- END-TO-END ANTI-SPOOFING WITH RAWNET2 [paper](https://arxiv.org/pdf/2011.01108.pdf) [code](https://github.com/eurecom-asp/rawnet2-antispoofing)

- Pushing the limits of raw waveform speaker recognition [paper](https://arxiv.org/pdf/2203.08488.pdf)



### using pretrained models

- Automatic speaker verification spoofing and deepfake detection using wav2vec 2.0 and data augmentation [paper](https://arxiv.org/pdf/2202.12233.pdf) 



## loss

- One-Class Learning Towards Synthetic Voice Spoofing Detection [paper](https://arxiv.org/pdf/2010.13995.pdf) [code](https://github.com/yzyouzhang/AIR-ASVspoof)
- 





## data augmentation

- Improved mixed-example data augmentation [paper](https://arxiv.org/pdf/1805.11272.pdf) [code](https://github.com/ceciliaresearch/MixedExample)

- RAWBOOST: A RAW DATA BOOSTING AND AUGMENTATION METHOD APPLIED TO AUTOMATIC SPEAKER VERIFICATION ANTI-SPOOFING [paper](https://arxiv.org/pdf/2111.04433.pdf) [code](https://github.com/TakHemlata/RawBoost-antispoofing)











# enlightening

- Your Out-of-Distribution Detection Method is Not Robust! [paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/1f6591cc41be737e9ba4cc487ac8082d-Paper-Conference.pdf)  [code](https://github.com/rohban-lab/ATD)
- Watermarking for Out-of-distribution Detection [paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)  [code](https://github.com/QizhouWang/watermarking)



### 2023

- DETECTING OUT-OF-DISTRIBUTION EXAMPLES VIA CLASS-CONDITIONAL IMPRESSIONS REAPPEARING  [paper](https://arxiv.org/pdf/2303.09746.pdf) 
- MCROOD: MULTI-CLASS RADAR OUT-OF-DISTRIBUTION DETECTION [paper](https://arxiv.org/pdf/2303.06232.pdf) 
- DO PROSODY TRANSFER MODELS TRANSFER PROSODY?  [paper](https://arxiv.org/pdf/2303.04289.pdf) 
- TWO-STREAM DECODER FEATURE NORMALITY ESTIMATING NETWORK FOR INDUSTRIAL ANOMALY DETECTION [paper](https://arxiv.org/pdf/2302.09794.pdf) 

