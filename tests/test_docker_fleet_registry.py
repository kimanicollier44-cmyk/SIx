import unittest
from src.docker_fleet_registry import (
    SNAPSHOT_DATE,
    STATUS_LIVE,
    STATUS_PENDING,
    all_images,
    get_image,
    live_images,
    pending_images,
    pull_command,
    registry_summary,
    top_images,
    total_pulls,
    total_stars,
)

class TestDockerFleetRegistry(unittest.TestCase):
    def test_record_counts(self):
        self.assertEqual(len(all_images()), 40)
        self.assertEqual(len(live_images()), 37)
        self.assertEqual(len(pending_images()), 3)

    def test_total_pulls(self):
        self.assertEqual(total_pulls(), 2262)

    def test_total_stars(self):
        self.assertEqual(total_stars(), 37)

    def test_top_image(self):
        top = top_images(1)
        self.assertEqual(len(top), 1)
        self.assertEqual(top[0].name, "superconductor-lab")
        self.assertEqual(top[0].pulls, 150)

    def test_top_images_ordering(self):
        pulls = [image.pulls for image in top_images(10)]
        self.assertEqual(pulls, sorted(pulls, reverse=True))

    def test_pull_command_format(self):
        self.assertEqual(pull_command("orbitx"), "docker pull credkellar/orbitx:latest")
        image = get_image("orbitx")
        self.assertEqual(image.ref, "credkellar/orbitx:latest")
        self.assertEqual(image.pull_command, "docker pull credkellar/orbitx:latest")

    def test_pull_command_pending(self):
        self.assertEqual(pull_command("six"), "docker pull credkellar/six:latest")

    def test_pending_images_have_no_counts(self):
        for image in pending_images():
            self.assertEqual(image.status, STATUS_PENDING)
            self.assertIsNone(image.pulls)
            self.assertIsNone(image.stars)

    def test_unknown_name_raises(self):
        with self.assertRaises(KeyError):
            pull_command("does-not-exist")
        with self.assertRaises(KeyError):
            get_image("does-not-exist")

    def test_live_records_sane(self):
        for image in live_images():
            self.assertEqual(image.status, STATUS_LIVE)
            self.assertGreater(image.pulls, 0)
            self.assertGreaterEqual(image.stars, 0)
            self.assertEqual(image.ref, f"credkellar/{image.name}:latest")
            self.assertEqual(image.pull_command, f"docker pull credkellar/{image.name}:latest")

    def test_registry_summary(self):
        summary = registry_summary()
        self.assertEqual(summary["snapshot_date"], SNAPSHOT_DATE)
        self.assertEqual(summary["total_images"], 40)
        self.assertEqual(summary["live_images"], 37)
        self.assertEqual(summary["pending_images"], 3)
        self.assertEqual(summary["total_pulls"], 2262)
        self.assertEqual(summary["total_stars"], 37)
        self.assertEqual(summary["top_image"], "superconductor-lab")

if __name__ == '__main__':
    unittest.main()
