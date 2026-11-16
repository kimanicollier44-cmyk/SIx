import unittest
import torch
from src.ani_agi_bridge import ANItoAGIUnifiedController
from src.continuous_meta_learner import ContinuousMetaLearner
from src.error_reduction_mesh import ErrorReducedNeuromorphicCore

class TestSiXMesh(unittest.TestCase):
    def test_ani_agi_bridge(self):
        controller = ANItoAGIUnifiedController(narrow_feature_dim=64, agi_latent_dim=32)
        v = torch.randn(2, 64)
        a = torch.randn(2, 64)
        p = torch.randn(2, 64)
        val = torch.randn(2, 32)
        out = controller(v, a, p, val)
        self.assertEqual(out.shape, (2, 32))

    def test_error_reduced_core(self):
        core = ErrorReducedNeuromorphicCore(in_features=64, out_features=32)
        spikes = torch.rand(2, 64)
        val = torch.randn(2, 32)
        out = core(spikes, val)
        self.assertEqual(out.shape, (2, 32))

if __name__ == '__main__':
    unittest.main()
