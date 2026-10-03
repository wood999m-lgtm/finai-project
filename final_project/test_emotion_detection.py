"""Unit tests for the emotion_detector function."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check that each statement returns the expected dominant emotion."""

    def test_emotion_detector(self):
        """Test the dominant emotion for five sample statements."""
        cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for text, expected in cases.items():
            self.assertEqual(emotion_detector(text)['dominant_emotion'], expected)


if __name__ == '__main__':
    unittest.main()
