# Banana Ripeness Classifier (CV12)

A binary image classifier that detects whether a banana is Green (Unripe) or Yellow (Ripe), built for GET 324 (AI/ML) mini-project.

## Live App
[Add your Streamlit link here]

## Dataset
Banana Ripeness Classification Dataset (Kaggle, by S.M. Shahriar) — filtered to the "unripe" (green) and "ripe" (yellow) classes only.

## Model
MobileNetV3Small (transfer learning), fine-tuned by unfreezing the top layers of the base network, and further improved with class weighting to correct imbalance between the two categories (1902 green vs 3522 yellow images).

## Performance
- Validation accuracy: ~100%
- Test set accuracy: ~100%
- Manual testing on external images (outside the training/test set) confirmed strong performance on clear, single-banana photos. A known limitation is reduced accuracy on complex images with multiple clustered bananas — see "Limitations" below.

## How to Use
1. Open the live app link above
2. Upload a clear photo of a banana (JPG or PNG)
3. View the prediction (Green/Yellow) with confidence percentages

## Limitations & Future Improvements
- The model assumes every uploaded image is a banana and will still output a prediction for non-banana images.
- Complex images (e.g., multiple bunched bananas) are harder to classify correctly than single bananas.
- Future work could include a more visually diverse training set, HSV-based color preprocessing, or a rejection mechanism for invalid/non-banana inputs.

## Files
- `app.py` — Streamlit application
- `banana_model.keras` — trained model
- `requirements.txt` — dependencies

## Contributors
- [Name: JOHN, NTIENSE UWEM [Reg No: 23/EG/CV/035 — GitHub: ntiensejohn459-cpu
- [Name: YOUR NAME [Reg No: 23/EG/CV/045 — GitHub: Didee968
- [Name: YOUR NAME [Reg No: YOUR REG.NO — GitHub: YOUR GITHUB USERNAME
- [Name: YOUR NAME [Reg No: YOUR REG.NO — GitHub: YOUR GITHUB USERNAME-
- [Name: YOUR NAME [Reg No: YOUR REG.NO — GitHub: YOUR GITHUB USERNAME
- [Name: YOUR NAME [Reg No: YOUR REG.NO — GitHub: YOUR GITHUB USERNAME
- [Name: YOUR NAME [Reg No: YOUR REG.NO — GitHub: YOUR GITHUB USERNAME
