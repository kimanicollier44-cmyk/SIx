"""Docker fleet image registry for the SIx secure mesh.

A frozen, offline catalogue of Darion Kellar's fleet Docker images
(namespace ``credkellar`` on Docker Hub), merged into SIx so the mesh
can report which container images the fleet has actually published.

The pull / star counts are a DATED SNAPSHOT, verified live from the
Docker Hub API on 2026-11-17 (see ``SNAPSHOT_DATE``). They are not live
telemetry: this module performs no network access and reads no clock,
so every function returns the same values on every run. Images that
are pushed to GitHub but not yet published on Docker Hub are listed
with status ``PENDING_PUBLISH`` and ``pulls=None`` -- no count is ever
invented for them.
"""
import logging
from dataclasses import dataclass
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

NAMESPACE = "credkellar"
SNAPSHOT_DATE = "2026-11-17"

STATUS_LIVE = "LIVE"
STATUS_PENDING = "PENDING_PUBLISH"


@dataclass(frozen=True)
class DockerImage:
    """One fleet Docker image record (immutable snapshot entry)."""
    name: str
    pulls: Optional[int]
    stars: Optional[int]
    status: str
    role: str

    @property
    def ref(self) -> str:
        return f"{NAMESPACE}/{self.name}:latest"

    @property
    def pull_command(self) -> str:
        return f"docker pull {self.ref}"


# --- Live images: verified on Docker Hub, 2026-11-17 (pulls, stars) ---
_LIVE = (
    DockerImage("superconductor-lab", 150, 1, STATUS_LIVE,
                "Superconductivity physics lab - critical fields, Meissner effect, Josephson models"),
    DockerImage("rate-limit-mask", 107, 1, STATUS_LIVE,
                "API rate-limit masking tool - provider auth-variable registry"),
    DockerImage("ai-jailbreak-re", 89, 1, STATUS_LIVE,
                "AI jailbreak reverse-engineering research lab (defensive study)"),
    DockerImage("dronehover-swarm", 88, 1, STATUS_LIVE,
                "Drone hover swarm coordination lab"),
    DockerImage("orbitx", 85, 1, STATUS_LIVE,
                "Sim-only orbital transport autopilot lab"),
    DockerImage("teleportnet-router", 74, 1, STATUS_LIVE,
                "Quantum teleportation network routing lab"),
    DockerImage("guardrailx", 74, 1, STATUS_LIVE,
                "AI guardrail / safety filter tool"),
    DockerImage("quantumtunnel-x", 71, 1, STATUS_LIVE,
                "Quantum tunnelling physics lab"),
    DockerImage("k3y-fo8", 70, 1, STATUS_LIVE,
                "Security key tooling lab"),
    DockerImage("bellpair-factory", 69, 1, STATUS_LIVE,
                "Bell pair generation / entanglement factory lab"),
    DockerImage("timecrystal-q", 67, 1, STATUS_LIVE,
                "Time crystal quantum physics lab"),
    DockerImage("hyperloop-lev", 67, 1, STATUS_LIVE,
                "Hyperloop levitation transport lab"),
    DockerImage("hoverboard-lab", 66, 1, STATUS_LIVE,
                "Hoverboard levitation physics lab"),
    DockerImage("hovercargo-x", 66, 1, STATUS_LIVE,
                "Heavy-lift hover cargo transport lab"),
    DockerImage("acousticlev-lab", 62, 1, STATUS_LIVE,
                "Acoustic levitation sound lab"),
    DockerImage("magchip-q", 62, 1, STATUS_LIVE,
                "Magnetic quantum chip computer lab"),
    DockerImage("casimirx", 61, 1, STATUS_LIVE,
                "Casimir effect vacuum physics lab"),
    DockerImage("qec-fortress", 60, 1, STATUS_LIVE,
                "Quantum error correction lab"),
    DockerImage("q6g-1tb", 58, 1, STATUS_LIVE,
                "Quantum 6G / high-throughput networking lab"),
    DockerImage("quantumannealer-lab", 55, 1, STATUS_LIVE,
                "Quantum annealing optimisation lab (classical simulation)"),
    DockerImage("quantumsensor-lab", 55, 1, STATUS_LIVE,
                "Quantum sensing lab - magnetometry, gravimetry, atomic clocks"),
    DockerImage("lte-6g", 53, 1, STATUS_LIVE,
                "LTE / 6G networking lab"),
    DockerImage("quantumrandom-lab", 51, 1, STATUS_LIVE,
                "Quantum randomness (QRNG) lab - simulation"),
    DockerImage("quantumbattery-lab", 50, 1, STATUS_LIVE,
                "Quantum battery charging and ergotropy lab"),
    DockerImage("hoverx", 48, 1, STATUS_LIVE,
                "Hover vehicle physics lab"),
    DockerImage("entanglenet-q", 48, 1, STATUS_LIVE,
                "Quantum entanglement network lab"),
    DockerImage("maglevx", 47, 1, STATUS_LIVE,
                "Maglev train levitation lab"),
    DockerImage("wormhole-lab", 47, 1, STATUS_LIVE,
                "Traversable wormhole physics lab"),
    DockerImage("proofclaim", 47, 1, STATUS_LIVE,
                "Claim verification lab - SHA-256 evidence, Merkle proofs, audit log"),
    DockerImage("nanobits-q", 47, 1, STATUS_LIVE,
                "Quantum nano-bits technology lab"),
    DockerImage("levitdock-x", 46, 1, STATUS_LIVE,
                "Levitation docking station lab"),
    DockerImage("levitationx", 43, 1, STATUS_LIVE,
                "Magnetic levitation physics lab"),
    DockerImage("plasmapropulsion-lab", 40, 1, STATUS_LIVE,
                "Ion and Hall thruster propulsion lab"),
    DockerImage("teleportcargo-sim", 36, 1, STATUS_LIVE,
                "Quantum teleportation cargo simulator"),
    DockerImage("spaceelevator-physics", 36, 1, STATUS_LIVE,
                "Space elevator tether physics lab"),
    DockerImage("gravwave-lab", 34, 1, STATUS_LIVE,
                "Gravitational wave astronomy lab"),
    DockerImage("subterrax", 33, 1, STATUS_LIVE,
                "Underground transport / tunnelling lab"),
)

# --- Pushed to GitHub, not yet published on Docker Hub (no counts) ---
_PENDING = (
    DockerImage("six", None, None, STATUS_PENDING,
                "SIx Gen-Intel Secure Mesh - this project"),
    DockerImage("quantum-synthetic-intelligence-cynefin-solver", None, None, STATUS_PENDING,
                "Quantum synthetic intelligence Cynefin sense-making solver lab"),
    DockerImage("bb-botx", None, None, STATUS_PENDING,
                "Bug bounty bot fleet lab"),
)

#: The full frozen registry: live images first (pulls descending), then pending.
DOCKER_FLEET_REGISTRY = _LIVE + _PENDING

_BY_NAME = {image.name: image for image in DOCKER_FLEET_REGISTRY}


def all_images() -> tuple:
    """Every registry record (live + pending), in registry order."""
    return DOCKER_FLEET_REGISTRY


def live_images() -> tuple:
    """Only the images live on Docker Hub in the snapshot."""
    return tuple(image for image in DOCKER_FLEET_REGISTRY if image.status == STATUS_LIVE)


def pending_images() -> tuple:
    """Only the images awaiting Docker Hub publication."""
    return tuple(image for image in DOCKER_FLEET_REGISTRY if image.status == STATUS_PENDING)


def get_image(name: str) -> DockerImage:
    """Look up one image by name; unknown names raise KeyError."""
    try:
        return _BY_NAME[name]
    except KeyError:
        raise KeyError(f"unknown fleet docker image: {name!r} "
                       f"(registry snapshot {SNAPSHOT_DATE}, {len(_BY_NAME)} images)") from None


def total_pulls() -> int:
    """Total pulls across LIVE images only (pending have no counts)."""
    return sum(image.pulls for image in live_images())


def total_stars() -> int:
    """Total stars across LIVE images only."""
    return sum(image.stars for image in live_images())


def top_images(n: int) -> tuple:
    """The n most-pulled live images, pulls descending (registry order breaks ties)."""
    ranked = sorted(live_images(), key=lambda image: -image.pulls)
    return tuple(ranked[:n])


def pull_command(name: str) -> str:
    """The `docker pull` command for one image; unknown names raise KeyError."""
    return get_image(name).pull_command


def registry_summary() -> dict:
    """Counts for the whole registry, stamped with the snapshot date."""
    return {
        "namespace": NAMESPACE,
        "snapshot_date": SNAPSHOT_DATE,
        "total_images": len(DOCKER_FLEET_REGISTRY),
        "live_images": len(live_images()),
        "pending_images": len(pending_images()),
        "total_pulls": total_pulls(),
        "total_stars": total_stars(),
        "top_image": top_images(1)[0].name,
    }
