# Tree Crown Detection using YOLOv8 (Baseline Model)

## 📌 Project Overview
This project focuses on **Tree Crown Detection** using **YOLOv8** as the baseline object detection model. The aim is to automatically identify and localize tree crowns from aerial or satellite imagery.

Tree crown detection is useful in:

- Forest monitoring  
- Tree population estimation  
- Urban greenery planning  
- Environmental analysis  
- Carbon stock estimation  
- Agricultural land management  

The current stage of the project includes:

✅ Dataset preparation  
✅ Handling `.tif` image format  
✅ Annotation setup  
✅ Baseline model training using YOLOv8  

---

## 🚀 Model Used

### YOLOv8 (Baseline)

We selected **YOLOv8** as the first baseline model because:

- Fast training and inference  
- Strong object detection performance  
- Easy customization  
- Supports custom datasets  
- Suitable for small and medium object detection tasks  

---

## 📂 Dataset Details

The dataset consists of **Tree Crown Images** in `.tif` format.

### Why `.tif` Format?

`.tif` images are commonly used in geospatial datasets because they provide:

- High image quality  
- Multi-band support  
- Better resolution than standard JPG/PNG  
- Suitable for aerial imagery  

### Dataset Preparation Completed

- Converted/processed `.tif` files for training compatibility  
- Organized dataset into:
  - `train/images`
  - `train/labels`
  - `val/images`
  - `val/labels`

- Annotation format converted to YOLO format

---

## 🛠️ Project Workflow

```text
Raw .tif Images
      ↓
Preprocessing
      ↓
Annotation / Label Conversion
      ↓
YOLO Dataset Structure
      ↓
YOLOv8 Baseline Training
      ↓
Evaluation
      ↓
Future Improvements
