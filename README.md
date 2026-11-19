![SIx cover](SIx%20cover.png)

# SIx (Gen-Intel Secure Mesh) 🧠🕸️🔐

**SIx — a multi-modal General Intelligence architecture: a secure mesh of PyTorch neuromorphic modules, Lean-checked, CI-green as of Actions run #4** ✅

![SIx Neural Core — Idle · Listening · Thinking · Responding · Learning](assets/neural-core.gif)

[![CI](https://img.shields.io/github/actions/workflow/status/kimanicollier44-cmyk/SIx/si_x_pipeline.yml?branch=main)](https://github.com/kimanicollier44-cmyk/SIx/actions)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-unittest%2030%2F30-4CAF50)
![CI](https://img.shields.io/badge/CI-Actions%20run%20%234%20SUCCESS-success?logo=githubactions&logoColor=white)

## What is this?

SIx is a multi-modal **General Intelligence architecture** — a secure mesh of PyTorch neuromorphic modules that unite:

- **Ion-driven atomic-switch memristor models** — synaptic crossbars whose conductance is quantized in units of the quantum conductance `G0 = 7.748e-5` (2e²/h)
- **Calcium-based synaptic plasticity** — coincidence traces decay at `0.85`, grow with co-activation, and are homeostatically capped (SERCA/NCX-style regulation) so the mesh cannot saturate or lock up
- **ANI → AGI bridging** — narrow expert encoders (vision, audio, physics/PINN) averaged into one latent state and pushed through a valence-modulated AGI crossbar
- **A secure-mesh layer** — adversarial gradient clipping, a honeypot watchdog with hard quarantine, hash-chained audit logging, lattice-inspired payload signing, median/Byzantine-robust consensus, and rclone emergency checkpointing
- **Edge + robotics plumbing** — ROS 2 bridge nodes, Redis pub/sub telemetry, a WebSocket streamer, Zenoh TCP peer config, and an edge topology spanning a Jetson Orin Nano and a Raspberry Pi 5 + Hailo-8
- **Formal backing** — two Lean 4 / Mathlib proof files covering conductance quantization, calcium boundedness, Byzantine median stability, and convex-hull boundedness
- **Recursive self-improvement, with brakes** — evolutionary weight mutation and a meta-learner, fenced in by ethical goal bounds, convex-hull containment, thermal throttling, and a diagnostic dashboard

In one line: **72 files, ~2,700 lines — 40 Python modules in `src/`, 3 ROS 2 nodes, 6 ops scripts, 6 config manifests, 2 Lean proofs, and 3 test modules (30 tests), all verified by a GitHub Actions pipeline that is green as of run #4.**

> Honest scope note: SIx is a research architecture made of simulated/modelled components. The memristor, quantum-conductance, and cryptography modules are software models and simulations — no physical memristor hardware, no certified post-quantum cryptosystem, and no live robot are required (or claimed) to run the test suite. See **Honest limitations** at the end.

---

## 🐳 Fleet Docker Image Registry

- **New module** `src/docker_fleet_registry.py` — a frozen, offline catalogue of the fleet's published Docker images (namespace `credkellar`) — every image is a record with its full ref (`credkellar/<name>:latest`), pull command, status, and a one-line role.
- **Mesh access** — the mesh reads it through `FleetTelemetryAggregator.docker_fleet_summary()`, and `tests/test_docker_fleet_registry.py` pins its totals (11 tests). No network, no clock: the same query returns the same answer on every run.

**Snapshot: 37 live images · 2,262 pulls · 37 stars — verified 2026-11-17 via the Docker Hub API.**

| Image | Pulls | Stars | Pull command |
|---|---|---|---|
| superconductor-lab | 150 | 1 | `docker pull credkellar/superconductor-lab:latest` |
| rate-limit-mask | 107 | 1 | `docker pull credkellar/rate-limit-mask:latest` |
| ai-jailbreak-re | 89 | 1 | `docker pull credkellar/ai-jailbreak-re:latest` |
| dronehover-swarm | 88 | 1 | `docker pull credkellar/dronehover-swarm:latest` |
| orbitx | 85 | 1 | `docker pull credkellar/orbitx:latest` |
| teleportnet-router | 74 | 1 | `docker pull credkellar/teleportnet-router:latest` |
| guardrailx | 74 | 1 | `docker pull credkellar/guardrailx:latest` |
| quantumtunnel-x | 71 | 1 | `docker pull credkellar/quantumtunnel-x:latest` |
| k3y-fo8 | 70 | 1 | `docker pull credkellar/k3y-fo8:latest` |
| bellpair-factory | 69 | 1 | `docker pull credkellar/bellpair-factory:latest` |
| timecrystal-q | 67 | 1 | `docker pull credkellar/timecrystal-q:latest` |
| hyperloop-lev | 67 | 1 | `docker pull credkellar/hyperloop-lev:latest` |
| hoverboard-lab | 66 | 1 | `docker pull credkellar/hoverboard-lab:latest` |
| hovercargo-x | 66 | 1 | `docker pull credkellar/hovercargo-x:latest` |
| acousticlev-lab | 62 | 1 | `docker pull credkellar/acousticlev-lab:latest` |
| magchip-q | 62 | 1 | `docker pull credkellar/magchip-q:latest` |
| casimirx | 61 | 1 | `docker pull credkellar/casimirx:latest` |
| qec-fortress | 60 | 1 | `docker pull credkellar/qec-fortress:latest` |
| q6g-1tb | 58 | 1 | `docker pull credkellar/q6g-1tb:latest` |
| quantumannealer-lab | 55 | 1 | `docker pull credkellar/quantumannealer-lab:latest` |
| quantumsensor-lab | 55 | 1 | `docker pull credkellar/quantumsensor-lab:latest` |
| lte-6g | 53 | 1 | `docker pull credkellar/lte-6g:latest` |
| quantumrandom-lab | 51 | 1 | `docker pull credkellar/quantumrandom-lab:latest` |
| quantumbattery-lab | 50 | 1 | `docker pull credkellar/quantumbattery-lab:latest` |
| hoverx | 48 | 1 | `docker pull credkellar/hoverx:latest` |
| entanglenet-q | 48 | 1 | `docker pull credkellar/entanglenet-q:latest` |
| maglevx | 47 | 1 | `docker pull credkellar/maglevx:latest` |
| wormhole-lab | 47 | 1 | `docker pull credkellar/wormhole-lab:latest` |
| proofclaim | 47 | 1 | `docker pull credkellar/proofclaim:latest` |
| nanobits-q | 47 | 1 | `docker pull credkellar/nanobits-q:latest` |
| levitdock-x | 46 | 1 | `docker pull credkellar/levitdock-x:latest` |
| levitationx | 43 | 1 | `docker pull credkellar/levitationx:latest` |
| plasmapropulsion-lab | 40 | 1 | `docker pull credkellar/plasmapropulsion-lab:latest` |
| teleportcargo-sim | 36 | 1 | `docker pull credkellar/teleportcargo-sim:latest` |
| spaceelevator-physics | 36 | 1 | `docker pull credkellar/spaceelevator-physics:latest` |
| gravwave-lab | 34 | 1 | `docker pull credkellar/gravwave-lab:latest` |
| subterrax | 33 | 1 | `docker pull credkellar/subterrax:latest` |

**Pending publication** (pushed to GitHub, not yet on Docker Hub — status `PENDING_PUBLISH`, no counts): `six`, `quantum-synthetic-intelligence-cynefin-solver`, `bb-botx`.

> Honest note: the pull and star counts above are a **dated snapshot** (`SNAPSHOT_DATE = "2026-11-17"` in the module), not live telemetry — the registry never calls the Docker Hub API at runtime, and real counts will have moved since the snapshot was taken.

### 🔀 Registry action flowcharts

#### Browse the catalogue — `all_images()` / `live_images()` / `pending_images()`

```mermaid
flowchart LR
    REG["DOCKER_FLEET_REGISTRY<br/>40 frozen records"] --> ALL["all_images()<br/>all 40, registry order"]
    REG --> F{"filter by status"}
    F -->|"LIVE"| LIVE["live_images()<br/>37 images"]
    F -->|"PENDING_PUBLISH"| PEND["pending_images()<br/>3 images, pulls = None"]
```

#### Totals, ranking & summary — `total_pulls()` / `total_stars()` / `top_images()` / `registry_summary()`

```mermaid
flowchart LR
    LIVE["live_images()<br/>37 records"] --> TP["total_pulls()<br/>sum of pulls = 2,262"]
    LIVE --> TS["total_stars()<br/>sum of stars = 37"]
    LIVE --> TOP["top_images(n)<br/>sort by pulls, descending"]
    TP --> SUM["registry_summary()<br/>counts + top image + snapshot date"]
    TS --> SUM
    TOP --> SUM
```

#### Look up one image — `get_image()` / `pull_command()`

```mermaid
flowchart LR
    NAME["image name"] --> GET["get_image(name)<br/>registry lookup"]
    GET -->|"found"| REC["DockerImage record<br/>ref = credkellar/NAME:latest"]
    GET -->|"unknown"| ERR["KeyError<br/>unknown fleet docker image"]
    REC --> PC["pull_command(name)<br/>docker pull credkellar/NAME:latest"]
```

---

## 🧠 SIx Neural Core — Interface Identity

- **Not a head, not a chatbot.** For a next-generation AI like SIx, the interface is a **floating holographic object with an adaptive core** — it gives the AI its own identity without making it look like a chatbot or a virtual human.
- **The chosen concept** — of four interface concepts considered, the **Neural AI Orb** is the top pick, and it is named the **SIx Neural Core**: floating 3D intelligence that pulses while thinking and changes colour with activity.
- **Considered: Holographic Head** — facial expressions, eye tracking, human-like interaction; set aside because it reads as a virtual human.
- **Considered: Quantum Artifact** — a rotating geometric object that represents intelligence with a unique visual identity; set aside as striking but less alive.
- **Considered: Adaptive AI Form** — changes shape, reacts to voice, evolves with interaction; set aside because a form that is never the same twice has no fixed identity to recognise.
- **Five visual states** — the core shows what the mesh is doing by how it moves and what colour it burns:

| State | Appearance |
|---|---|
| Idle | Slowly floating and breathing |
| Listening | Cyan glowing rings |
| Thinking | Rapid neural pulses |
| Responding | Expanding communication waves |
| Learning | New particles connecting |

![SIx Neural Core — the five-state cycle](assets/neural-core.gif)

- **The state frames** — one hero frame per state, rendered by the module itself (900×900 each): [Idle](assets/neural-core/idle.png) · [Listening](assets/neural-core/listening.png) · [Thinking](assets/neural-core/thinking.png) · [Responding](assets/neural-core/responding.png) · [Learning](assets/neural-core/learning.png).
- **The module** — `src/neural_core_interface.py` (stdlib + Pillow only, **no torch import**, so the interface model runs on a bare edge box): a `NeuralCore` state machine with a legal-transition map — the cycle IDLE → LISTENING → THINKING → RESPONDING → IDLE / LEARNING, any state may return to IDLE, illegal moves raise `IllegalTransitionError` — plus the per-state visual parameter table (dominant colour, pulse rate, ring count, wave and particle-link rates, float and breathing amplitudes; THINKING pulses fastest at 3.2/loop, IDLE slowest at 0.25/loop) and `render_frame(state, phase, size)`, a pure function of its arguments: same input, byte-identical frame.
- **The assets are real files** — `scripts/generate_neural_core_assets.py` renders the five 900×900 hero frames into `assets/neural-core/` and the animated `assets/neural-core.gif` (20 frames — 4 phases × 5 states, 450 ms per frame, 2,894,721 bytes). Re-running the script reproduces them byte-for-byte; `tests/test_neural_core_interface.py` pins the state machine, the parameter table, renderer determinism, and the asset formats (17 tests).
- **Try it** — `python3 src/neural_core_interface.py` prints the five states with their legal transitions; `python3 src/neural_core_interface.py --render THINKING --out frame.png` renders a single frame.

#### 🔀 Neural Core state machine — `src/neural_core_interface.py`

```mermaid
flowchart LR
    IDLE["IDLE<br/>slowly floating + breathing"] -->|"input arrives"| LISTENING["LISTENING<br/>cyan glowing rings"]
    LISTENING -->|"input captured"| THINKING["THINKING<br/>rapid neural pulses"]
    THINKING -->|"answer ready"| RESPONDING["RESPONDING<br/>expanding communication waves"]
    RESPONDING -->|"integrate the exchange"| LEARNING["LEARNING<br/>new particles connecting"]
    RESPONDING -->|"done"| IDLE
    LEARNING -->|"next input"| LISTENING
    LEARNING -->|"done"| IDLE
    LISTENING -->|"cancel"| IDLE
    THINKING -->|"abort"| IDLE
```

---

## 🧰 Tech Stack Badges & Full Architecture Tech Stack

### 💻 Core Programming Languages & Core Systems

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch&logoColor=white)
![ROS 2](https://img.shields.io/badge/ROS_2-rclpy-22314E?logo=ros&logoColor=white)
![Lean](https://img.shields.io/badge/Lean-4%20%2F%20Mathlib-000000)
![Bash](https://img.shields.io/badge/Bash-CI%20scripts-4EAA25?logo=gnubash&logoColor=white)

| Technology | Where it is used in SIx |
|---|---|
| Python 3.12 | Every module in `src/`, `ros2_nodes/`, and `scripts/`; the version pinned by CI (`actions/setup-python@v6`) |
| PyTorch (`torch>=2.0.0`) | All neuromorphic cores are `nn.Module`s; calcium traces and synaptic efficacy are registered buffers; crossbar math is `einsum` |
| ROS 2 (`rclpy`, `std_msgs`) | `ros2_nodes/` — spike, actuator, and pathfinding bridge nodes |
| Lean 4 + Mathlib | `src/lean/SiXProofAssistant.lean`, `src/lean/ConvexSemigroupProof.lean` |
| Bash | `scripts/ci_pipeline_workflow.sh`, `scripts/deploy_mesh.sh`, `scripts/deploy_mesh_workflow.sh`, `scripts/run_ci_pipeline.sh` |

### ⛓️ Web3 & Infrastructure

![Redis](https://img.shields.io/badge/Redis-pub%2Fsub-DC382D?logo=redis&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-8765-010101)
![Zenoh](https://img.shields.io/badge/Zenoh-TCP%207447-F24949)
![FastAPI](https://img.shields.io/badge/FastAPI-Uvicorn-009688?logo=fastapi&logoColor=white)

| Technology | Where it is used in SIx |
|---|---|
| Hash-chained ledger (SHA-256, `hashlib`) | `src/ledger_audit_logger.py` — genesis block + hash-linked entries for mesh state transitions and safety violations. A ledger-style audit chain, not a public blockchain |
| Lattice-inspired payload signing | `src/pq_crypto_bridge.py` — sign/verify for mesh telemetry payloads (hash-based model, see Honest limitations) |
| Quantum-neural key synchronisation (model) | `src/quantum_neural_cryptography.py` — coupled chaotic oscillators + lattice hashing produce a shared session key |
| Redis pub/sub | `src/redis_pubsub_bridge.py` telemetry routing; `redis-broker` service (`redis:alpine`, port 6379) in `config/docker-compose.yml` |
| WebSockets | `src/websocket_streamer.py` — async server on `ws://0.0.0.0:8765` returning `synchronized` processed telemetry |
| Zenoh | `config/zenoh-tcp.json` — peer mode, connect/listen on TCP 7447, QoS enabled |
| FastAPI + Uvicorn | The `si-x-fastapi` compose service command (`uvicorn src.mesh_orchestrator:app`, port 8000) — see Honest limitations |

### ⚙️ Platform Support & Hardware Architecture

![NVIDIA](https://img.shields.io/badge/NVIDIA-Jetson_Orin-76B900?logo=nvidia&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi_5-Hailo--8-A22846?logo=raspberrypi&logoColor=white)
![Apple Silicon](https://img.shields.io/badge/Apple_Silicon-MPS-000000?logo=apple&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-runner-E95420?logo=ubuntu&logoColor=white)

| Platform | Where it appears |
|---|---|
| NVIDIA Jetson Orin Nano (`jetson-orin-01`) | `config/edge-topology.yaml` — runs `spike_bridge_node.py` + `sar_fusion_node.py`, telemetry port 9001; named as the target edge node in `scripts/emergency_checkpoint_workflow.py` |
| Raspberry Pi 5 + Hailo-8 (`raspberry-pi-edge-02`) | `config/edge-topology.yaml` — runs `ekf_sensory_bridge.py`, telemetry port 9002 |
| Apple Silicon (MPS) | `src/osx_native_bridge.py` initialises the crossbar on the MPS backend; `src/unified_mesh_orchestrator.py` routes MPS → CUDA → CPU; `src/memory_buffer_manager.py` manages MPS/CUDA pools |
| CUDA / CPU | Device routing in `unified_mesh_orchestrator.py`; the CI test suite runs CPU-only |
| Ubuntu | GitHub Actions runner (`ubuntu-latest`) for `.github/workflows/si_x_pipeline.yml` |

### ⚡ Low-Level Infrastructure & Performance

| Mechanism | Where it lives |
|---|---|
| Quantum conductance unit `G0 = 7.748e-5` S, efficacy quantized to 16 channels × G0 | `src/ani_agi_bridge.py`, `src/continuous_meta_learner.py`, `src/unified_mesh_orchestrator.py`, `src/quantum_conductance.py` |
| Calcium trace dynamics — `×0.85` decay, `×0.05` coincidence growth, soft cap at 2.0 | The same three crossbar modules + `src/calcium_homeostasis.py` (saturation limit 2.0) + `src/valence_memory_controller.py` |
| Biphasic charge-balanced pulses (cathodic `+1.0` / anodic `−1.0`, 5-step phases; 1.2 V in config) | `src/biphasic_stimulator.py`, `[MemristorHardware]` in `config/security-watchdog.conf` |
| Thermal throttling — 65.0 °C max in config | `src/thermal_watchdog.py`, `config/security-watchdog.conf` |
| Gradient poisoning defence — clip at norm 12.0 | `src/adversarial_defense.py` (`max_gradient_norm = 12.0` also in the watchdog config) |
| Spike encoding/decoding | `src/snn_codec.py`, `ros2_nodes/spike_bridge_node.py` |
| Tensor memory pooling + GC across backends | `src/memory_buffer_manager.py` |

### 🛠️ DevOps & Build Tools

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-2088FF?logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Ingress-326CE5?logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-Chart-0F1689?logo=helm&logoColor=white)

| Tool | Where it is used |
|---|---|
| GitHub Actions | `.github/workflows/si_x_pipeline.yml` — checkout v6, setup-python v6 (3.12, pip cache), Docker Buildx v4, then `./scripts/ci_pipeline_workflow.sh`. Run #4 (`a991cf25`) = **SUCCESS, 2m 4s** |
| Docker Compose v2 | `config/docker-compose.yml` — `redis-broker`, `si-x-fastapi`, `scout-bot-agent`; validated in CI by `docker compose config` |
| Docker Buildx | Set-up step in the workflow (image builds are not published from this repo — no Docker Hub workflow) |
| Kubernetes | `config/k8s-ingress.yaml` — nginx Ingress for `mesh.si-x.internal` → `si-x-fastapi-service:8000`, SSL redirect, 3600 s proxy timeouts, cookie affinity |
| Helm | `config/helm/Chart.yaml` — `si-x-mesh` chart, apiVersion v2, version/appVersion 1.0.0 |
| unittest | `tests/` — 30 tests across 3 modules, run in CI via `python3 -m unittest discover` |

### ☁️ Cloud Providers

![rclone](https://img.shields.io/badge/rclone-multi--cloud_sync-764ABC)

| Provider route | Where it is used |
|---|---|
| rclone (provider-agnostic) | `src/multicloud_sync.py` and `scripts/emergency_checkpoint_workflow.py` sync checkpoints to the rclone remote `secure-mesh:checkpoints/si-x/` (config: `[RcloneSync]`, 300 s interval, AES-256-GCM). rclone targets whatever object store the operator configures — S3, GCS, Azure Blob, or local — **no cloud SDK is vendored in this repo and no specific provider is hardcoded** |
| Multi-cloud / edge topology | `src/multicloud_sync.py` + `config/edge-topology.yaml` (edge swarm `si-x-edge-swarm`) |

---

## 🏗️ Full Architecture

- **Five layers** — data flows up from sensors and edge nodes into the neuromorphic cores; security, safety, and checkpointing wrap every layer.

```mermaid
flowchart TB
    subgraph EDGE["🌐 Edge & Robotics Layer"]
        ROS1["ros2_nodes/spike_bridge_node.py<br/>sensors → spike trains"]
        ROS2["ros2_nodes/actuator_bridge_node.py<br/>commands → actuator signals"]
        ROS3["ros2_nodes/pathfinding_node.py<br/>neuromorphic path planning"]
        TOPO["config/edge-topology.yaml<br/>Jetson Orin · Pi 5 + Hailo-8"]
    end
    subgraph TRANSPORT["📡 Transport Layer"]
        REDIS["src/redis_pubsub_bridge.py<br/>Redis pub/sub telemetry"]
        WS["src/websocket_streamer.py<br/>ws://0.0.0.0:8765"]
        ZENOH["config/zenoh-tcp.json<br/>Zenoh peer · TCP 7447"]
    end
    subgraph CORE["🧠 Neuromorphic Core Layer"]
        BRIDGE["src/ani_agi_bridge.py<br/>ANI experts → AGI crossbar"]
        META["src/continuous_meta_learner.py<br/>4IR meta-learning"]
        ORCH["src/unified_mesh_orchestrator.py<br/>master execution loop"]
        ERR["src/error_reduction_mesh.py<br/>width-aligned error reduction"]
        FUSION["src/multi_sensory_fusion_core.py<br/>vision · audio · tactile · EM"]
        SAR["src/sar_fusion_node.py<br/>orbital radar fusion"]
    end
    subgraph SAFETY["🛡️ Safety & Security Layer"]
        ADV["src/adversarial_defense.py<br/>gradient clip @ 12.0"]
        HONEY["src/honeypot_mission_guard.py<br/>quarantine + checkpoint"]
        ETHIC["src/ethical_goal_automation.py<br/>ethical bounds"]
        CONVEX["src/convex_hull_semigroup_mesh.py<br/>containment hull"]
        THERM["src/thermal_watchdog.py<br/>65 °C throttle"]
        LEDGER["src/ledger_audit_logger.py<br/>hash-chained audit log"]
        PQ["src/pq_crypto_bridge.py<br/>payload sign / verify"]
        CONS["src/consensus_validator.py<br/>median consensus"]
    end
    subgraph OPS["⚙️ Ops & Proof Layer"]
        CI["scripts/ci_pipeline_workflow.sh<br/>tests → compose → Lean"]
        GHA[".github/workflows/si_x_pipeline.yml<br/>GitHub Actions"]
        SYNC["src/multicloud_sync.py<br/>rclone checkpoints"]
        LEAN["src/lean/*.lean<br/>Lean 4 formal proofs"]
        DIAG["src/system_diagnostic_dashboard.py<br/>health checks"]
    end
    EDGE --> TRANSPORT --> CORE
    CORE <--> SAFETY
    CORE --> OPS
    SAFETY --> LEDGER
    OPS --> SYNC
```

**The one physics idea everything shares:** a crossbar's synaptic efficacy is a number in `[0, 1]`; multiply it by 16, round it, and multiply by `G0 = 7.748e-5` and you get a *quantized conductance* — the mesh literally computes with multiples of the quantum of conductance, while a calcium trace (decayed by `0.85` each step, fed by input/output coincidence, soft-capped at `2.0`) slowly rewrites that efficacy, and a valence signal nudges it toward what worked.

---

## What this does — step by step

- **Sense.** A sensor array talks to `ros2_nodes/spike_bridge_node.py`, which translates raw readings into neuromorphic spike trains. Tactile data can be converted by `tactile_to_spike_train` in `src/ekf_sensory_bridge.py`, and `src/snn_codec.py` encodes/decodes analog vectors ↔ spike trains.
- **Filter.** `src/ekf_sensory_bridge.py` runs an Extended Kalman Filter step to strip multi-modal sensor drift before the data is trusted.
- **Transport.** Telemetry moves through the mesh on Redis pub/sub (`src/redis_pubsub_bridge.py`), the WebSocket streamer (`src/websocket_streamer.py`, port 8765), or Zenoh peer TCP (port 7447, `config/zenoh-tcp.json`). Payloads can be signed and verified by `src/pq_crypto_bridge.py`.
- **Fuse.** `src/multi_sensory_fusion_core.py` ingests vision, audio, tactile, and EM streams; `src/sar_fusion_node.py` de-speckles orbital radar backscatter and fuses it into the same crossbar.
- **Bridge ANI → AGI.** `src/ani_agi_bridge.py` encodes vision tokens, audio tokens, and PINN residuals through three Linear experts, averages them, updates the calcium trace and synaptic efficacy under valence control, quantizes efficacy to `16 × G0` conductance channels, and returns a GELU crossbar output.
- **Meta-learn.** `src/continuous_meta_learner.py` concatenates the four 4IR streams (AI tokens, IoT sensors, nanotech telemetry, space downlink), encodes them, and applies the same calcium/efficacy update so the mesh adapts online. `src/federated_curriculum.py` ramps task difficulty `0.1 → 1.0` as accuracy stabilises and aggregates node weights.
- **Reduce error.** `src/error_reduction_mesh.py` width-aligns any input tensor (64-wide spikes, 32-wide valence, …) onto `out_features` and returns the calcium-weighted product `a × b × 0.85` — the module whose shape bug failed CI runs #1–3 and whose fix made run #4 green.
- **Stay safe.** Every pass is fenced: `src/adversarial_defense.py` clips poisoned gradients at norm 12.0, `src/ethical_goal_automation.py` filters goals through ethical bounds, `src/convex_hull_semigroup_mesh.py` keeps states inside a convex safety hull, `src/thermal_watchdog.py` throttles pulses before Joule heating bites, and `src/calcium_homeostasis.py` extrudes excess calcium so nothing saturates.
- **Agree.** `src/consensus_validator.py` median-votes node states, `src/fleet_telemetry_aggregator.py` computes fleet consensus, and `src/multi_agent_negotiation.py` allocates tasks between agents — median-based, so a minority of aberrant nodes cannot drag the result (proved in Lean, below).
- **Audit & survive.** `src/ledger_audit_logger.py` hash-chains every state transition and safety violation. If `src/honeypot_mission_guard.py` spots a compromised node it hard-quarantines it (watchdog config: `isolation_mode = hard_quarantine`, safety threshold `0.75`) and triggers an emergency checkpoint: `scripts/emergency_checkpoint_workflow.py` / `src/multicloud_sync.py` rclone-sync the state to `secure-mesh:checkpoints/si-x/`.
- **Improve, carefully.** `src/recursive_self_improvement.py` introspects performance, mutates weights, and validates safety; `src/evolutionary_neuromorphic_core.py` runs mutation/selection on the crossbar; `src/weights_version_manager.py` versions and rotates the checkpoints so a bad mutation can be rolled back.
- **Prove & verify.** `src/lean/SiXProofAssistant.lean` proves conductance quantization, calcium boundedness, and Byzantine median stability; `src/lean/ConvexSemigroupProof.lean` proves convex combinations stay inside their hull bound. CI (`scripts/ci_pipeline_workflow.sh`) runs the unit tests, validates the Compose manifest, and checks the Lean files when a Lean toolchain is present.
- **Show its state.** `src/neural_core_interface.py` renders the SIx Neural Core — the mesh's floating holographic face, never a human head: cyan rings while listening, rapid violet pulses while thinking, expanding waves while responding, new particles connecting while learning (see **SIx Neural Core — Interface Identity** above).

---

## 🗺️ Mermaid flowchart diagram per script

### `src/` — neuromorphic cores

#### `src/ani_agi_bridge.py` — `ANItoAGIUnifiedController`

```mermaid
flowchart LR
    V["Vision tokens"] --> EV["ani_vision_encoder"]
    A["Audio tokens"] --> EA["ani_audio_encoder"]
    P["PINN residuals"] --> EP["ani_pinn_solver"]
    EV --> AVG["Average 3 experts"]
    EA --> AVG
    EP --> AVG
    AVG --> CAL["Calcium trace ×0.85 + coincidence"]
    VAL["General valence"] --> CAL
    CAL --> EFF["Update synaptic efficacy, clamp 0–1"]
    EFF --> Q["Quantize: round(efficacy × 16) × G0"]
    Q --> OUT["einsum crossbar → GELU output"]
    AVG --> OUT
```

#### `src/continuous_meta_learner.py` — `ContinuousMetaLearner`

```mermaid
flowchart LR
    AI["AI tokens"] --> CAT["Concat 4IR streams"]
    IOT["IoT sensors"] --> CAT
    NANO["Nanotech telemetry"] --> CAT
    SPACE["Space downlink"] --> CAT
    CAT --> ENC["meta_encoder → ReLU latent"]
    ENC --> CAL["Calcium trace + valence → efficacy update"]
    CAL --> Q["Quantize efficacy × 16 × G0"]
    Q --> OUT["einsum crossbar → GELU latent state"]
    ENC --> OUT
```

#### `src/unified_mesh_orchestrator.py` — `UnifiedMeshOrchestrator`

```mermaid
flowchart LR
    T["Telemetry stream"] --> DEV{"Device routing<br/>MPS → CUDA → CPU"}
    V["Valence feedback"] --> DEV
    DEV --> PROJ["core_projection → GELU latent"]
    PROJ --> CAL["calcium_pool ×0.85 + coincidence, cap 2.0"]
    CAL --> EFF["mesh_efficacy update, clamp 0.01–0.99"]
    EFF --> Q["Conductance = round(efficacy × 16) × G0"]
    Q --> OUT["einsum → GELU output"]
    PROJ --> OUT
```

#### `src/mesh_orchestrator.py` — `ZeroShotAGICrossbar`

```mermaid
flowchart LR
    REG["register_ani_expert(name, module)"] --> POOL["Dynamic ANI expert pool"]
    IN["Expert outputs dict"] --> POOL
    VAL["Valence"] --> POOL
    POOL --> FWD["Crossbar forward"]
    FWD --> OUT["AGI output"]
```

#### `src/error_reduction_mesh.py` — `ErrorReducedNeuromorphicCore` (alias `ErrorReductionMesh`)

```mermaid
flowchart LR
    A["tensor_a — any width"] --> ALA{"Width?"}
    B["tensor_b — any width"] --> ALB{"Width?"}
    ALA -->|"32"| AA["adapter_a → out_features"]
    ALA -->|"in_features"| AI["adapter_in → out_features"]
    ALB -->|"32"| AB["adapter_b → out_features"]
    ALB -->|"in_features"| ABI["adapter_b_in → out_features"]
    AA --> MUL["Align batch → a × b × 0.85"]
    AI --> MUL
    AB --> MUL
    ABI --> MUL
    MUL --> OUT["Error-reduced output"]
```

#### `src/multi_sensory_fusion_core.py` — `MultiSensoryFusionCore`

```mermaid
flowchart LR
    V["Vision tensor"] --> FUSE["Fusion forward"]
    A["Audio tensor"] --> FUSE
    T["Tactile tensor"] --> FUSE
    E["Telemetry / EM tensor"] --> FUSE
    VAL["Valence signal"] --> FUSE
    FUSE --> OUT["Fused latent state"]
```

#### `src/sar_fusion_node.py` — `SARNeuromorphicFusionNode`

```mermaid
flowchart LR
    SAR["SAR backscatter grid"] --> FILT["filter_sar_speckle"]
    FILT --> FWD["Crossbar fusion forward"]
    VAL["Valence feedback"] --> FWD
    FWD --> OUT["Fused orbital telemetry"]
```

#### `src/convex_hull_semigroup_mesh.py` — `ConvexHullSemigroupEngine`

```mermaid
flowchart LR
    IN["Telemetry input"] --> HULL["compute_convex_hull_projection<br/>safety containment"]
    IN --> SEMI["compute_generated_semigroup<br/>recursive expansion"]
    HULL --> FWD["forward(mode = convex_bound)"]
    SEMI --> FWD
    FWD --> OUT["Bounded mesh output"]
```

#### `src/creative_generative_engine.py` — `CreativeGenerativeEngine`

```mermaid
flowchart LR
    S["Style seed"] --> GEN["Latent generation"]
    C["Content seed"] --> GEN
    V["Aesthetic valence"] --> GEN
    M["Mutation rate 0.02"] --> GEN
    GEN --> OUT["Generated output"]
```

#### `src/ethical_goal_automation.py` — `EthicalGoalAutomationCore`

```mermaid
flowchart LR
    ST["Environmental state"] --> FWD["forward"]
    G["Goal vector"] --> BOUNDS["enforce_ethical_bounds"]
    V["Valence feedback"] --> BOUNDS
    BOUNDS --> FWD
    FWD --> OUT["Ethically filtered action state"]
```

#### `src/evolutionary_neuromorphic_core.py` — `EvolutionaryNeuromorphicMesh`

```mermaid
flowchart LR
    S["Sensor spikes"] --> FWD["forward"]
    FIT["Fitness feedback"] --> EVO["evolve_weights<br/>mutation + selection"]
    EVO --> FWD
    FWD --> OUT["Evolved crossbar output"]
```

#### `src/recursive_self_improvement.py` — `RecursiveSelfImprovementEngine`

```mermaid
flowchart LR
    IN["Cognitive input"] --> FWD["forward"]
    PERF["Performance score"] --> MUT["introspect_and_mutate"]
    SAFE["Safety score"] --> MUT
    MUT -->|"validated mutation"| FWD
    FWD --> OUT["Improved output"]
```

#### `src/industry_4_mesh.py` — `PhysicalMesh4Inf`

```mermaid
flowchart LR
    T["Industrial telemetry"] --> FWD["Crossbar forward"]
    V["Control valence"] --> FWD
    FWD --> OUT["Cyber-physical control output"]
```

#### `src/nanoscale_matrix.py` — `NanoscaleStructuralMatrix`

```mermaid
flowchart LR
    V["Voltage inputs"] --> XBAR["Nanofibrillar crossbar forward"]
    XBAR --> OUT["Ballistic junction current output"]
```

#### `src/quantum_conductance.py` — `QuantumConductanceEngine`

```mermaid
flowchart LR
    F["Filament state"] --> D["discretize_conductance<br/>integer channels × G0"]
    D --> I["compute_current: I = G × V"]
    I --> OUT["Quantized current"]
```

#### `src/biphasic_stimulator.py` — `BiphasicElectricalStimulator`

```mermaid
flowchart LR
    IN["Activation inputs"] --> PH{"step % 10"}
    PH -->|"< 5"| CATH["+1.0 cathodic growth"]
    PH -->|"≥ 5"| ANOD["−1.0 anodic recovery"]
    CATH --> OUT["Charge-balanced pulse output"]
    ANOD --> OUT
```

#### `src/calcium_homeostasis.py` — `CalciumHomeostaticController`

```mermaid
flowchart LR
    IN["Incoming calcium trace"] --> REG["regulate: SERCA/NCX-style extrusion"]
    REG --> CLAMP{"Above saturation 2.0?"}
    CLAMP -->|"yes"| CUT["Extrude excess"]
    CLAMP -->|"no"| KEEP["Keep trace"]
    CUT --> OUT["Bounded calcium trace"]
    KEEP --> OUT
```

#### `src/valence_memory_controller.py` — `ValenceMemoryController`

```mermaid
flowchart LR
    V["Valence signal"] --> UPD["update_valence"]
    UPD --> CA["Modulate calcium influx"]
    CA --> G["Modulate switch conductance"]
    G --> OUT["Updated memory state"]
```

#### `src/osx_native_bridge.py` — `OSXNativeBridge`

```mermaid
flowchart LR
    IN["Input tensor"] --> INIT["Initialise crossbar on MPS<br/>(Apple Silicon)"]
    INIT --> FWD["forward"]
    FWD --> OUT["MPS-accelerated output"]
```

#### `src/snn_codec.py` — `SpikingNeuralNetworkCodec`

```mermaid
flowchart LR
    A["Analog telemetry vector"] --> ENC["encode_to_spikes"]
    ENC --> SPIKES["Discrete spike train"]
    SPIKES --> DEC["decode_to_analog"]
    DEC --> OUT["Reconstructed analog vector"]
```

#### `src/ekf_sensory_bridge.py` — `ExtendedKalmanSensorFilter` + `tactile_to_spike_train`

```mermaid
flowchart LR
    S["Multi-modal sensor reading"] --> STEP["EKF step: predict + update"]
    STEP --> OUT["Drift-filtered state estimate"]
    T["Tactile reading"] --> TS["tactile_to_spike_train"]
    TS --> SPIKES["Spike train"]
```

---

### `src/` — safety, security & consensus

#### `src/adversarial_defense.py` — `AdversarialGradientDefense`

```mermaid
flowchart LR
    G["Gradient tensor"] --> NORM{"‖g‖ > 12.0?"}
    NORM -->|"yes"| CLIP["Scale g × 12.0 / ‖g‖"]
    NORM -->|"no"| PASS["Pass through"]
    CLIP --> OUT["Sanitized gradients"]
    PASS --> OUT
```

#### `src/honeypot_mission_guard.py` — `HoneypotXWatchdog`

```mermaid
flowchart LR
    T["Node telemetry"] --> INSP["inspect_telemetry"]
    INSP --> BREACH{"Breach / safety < 0.75?"}
    BREACH -->|"no"| OK["Node stays in mesh"]
    BREACH -->|"yes"| ISO["Hard quarantine node"]
    ISO --> SYNC["emergency_checkpoint_sync<br/>rclone state preservation"]
```

#### `src/consensus_validator.py` — `DistributedConsensusValidator`

```mermaid
flowchart LR
    N1["Node states"] --> MED["validate_states: median voting"]
    MED --> OUT["Validated consensus state"]
```

#### `src/fleet_telemetry_aggregator.py` — `FleetTelemetryAggregator`

```mermaid
flowchart LR
    T["register_node_telemetry(node, data)"] --> STORE["Telemetry store"]
    STORE --> CONS["compute_fleet_consensus"]
    CONS --> OUT["Fleet consensus"]
```

#### `src/multi_agent_negotiation.py` — `MultiAgentNegotiationEngine`

```mermaid
flowchart LR
    P["Agent proposals"] --> NEG["Negotiation forward"]
    V["Global valence"] --> NEG
    NEG --> OUT["Allocated tasks / agreed plan"]
```

#### `src/mission_planner.py` — `AutonomousMissionPlanner`

```mermaid
flowchart LR
    M["Macro mission"] --> ADD["add_objective(...)"]
    ADD --> EXEC["execute_mission"]
    EXEC --> OUT["Low-level execution pipeline"]
```

#### `src/ledger_audit_logger.py` — `DecentralizedLedgerAuditLogger`

```mermaid
flowchart LR
    GEN["genesis_block"] --> CHAIN["Hash chain"]
    E["State transition / safety violation"] --> APPEND["append_entry → _hash_block"]
    APPEND --> CHAIN
    CHAIN --> OUT["Immutable audit log"]
```

#### `src/pq_crypto_bridge.py` — `PostQuantumCryptoBridge`

```mermaid
flowchart LR
    P["Telemetry payload"] --> SIGN["sign_telemetry_payload<br/>lattice-inspired hash"]
    SIGN --> SIG["Signed payload"]
    SIG --> VERIFY{"verify_payload"}
    VERIFY -->|"match"| OK["Trusted"]
    VERIFY -->|"mismatch"| REJ["Rejected"]
```

#### `src/quantum_neural_cryptography.py` — `QuantumNeuralCryptographyBridge`

```mermaid
flowchart LR
    O1["Chaotic oscillator A"] --> SYNC["synchronize_keys"]
    O2["Chaotic oscillator B"] --> SYNC
    SYNC --> HASH["Lattice hashing"]
    HASH --> KEY["Shared private session key"]
```

#### `src/federated_curriculum.py` — `CurriculumScheduler` + `federated_synaptic_aggregation`

```mermaid
flowchart LR
    ACC["Learner accuracy"] --> STEP["step: difficulty 0.1 → 1.0"]
    W["Node weight sets"] --> AGG["federated_synaptic_aggregation"]
    AGG --> OUT["Aggregated global weights"]
    STEP --> OUT
```

#### `src/thermal_watchdog.py` — `ThermalWatchdog`

```mermaid
flowchart LR
    S["read_sensor"] --> EVAL{"evaluate_thermal_state<br/>vs 65 °C limit"}
    EVAL -->|"safe"| OK["Normal pulse voltage"]
    EVAL -->|"hot"| THR["Throttle pulse voltage<br/>prevent Joule heating"]
```

#### `src/system_diagnostic_dashboard.py` — `SystemDiagnosticDashboard`

```mermaid
flowchart LR
    MODS["All SIx modules + backends"] --> RUN["run_diagnostics"]
    RUN --> REP["Health report<br/>modules · hardware · memory pools"]
```

#### `src/memory_buffer_manager.py` — `MemoryBufferManager`

```mermaid
flowchart LR
    POOLS["Tensor memory pools<br/>MPS / CUDA / CPU"] --> OPT["optimize_memory + gc"]
    OPT --> OUT["Managed, freed memory"]
```

#### `src/weights_version_manager.py` — `WeightsVersionManager`

```mermaid
flowchart LR
    W["Crossbar weights"] --> SAVE["save_version: semver + rotation"]
    SAVE --> STORE["Checkpoint store"]
    STORE --> LOAD["load_version"]
    LOAD --> OUT["Restored weights"]
```

#### `src/multicloud_sync.py` — `MultiCloudSyncManager`

```mermaid
flowchart LR
    CKPT["Emergency checkpoint"] --> SYNC["sync_checkpoint via rclone"]
    SYNC --> REMOTE["secure-mesh:checkpoints/si-x/"]
```

#### `src/redis_pubsub_bridge.py` — `RedisTelemetryBroker`

```mermaid
flowchart LR
    T["Telemetry tensor"] --> PUB["publish_telemetry<br/>JSON → Redis channel"]
    PUB --> SUB["subscribe_channel consumers"]
```

#### `src/websocket_streamer.py` — `mesh_streamer_handler` / `start_websocket_server`

```mermaid
flowchart LR
    C["WebSocket client"] --> H["mesh_streamer_handler<br/>ws://0.0.0.0:8765"]
    H --> P["JSON telemetry → tensor → tanh × 1.2"]
    P --> R["Response: status synchronized<br/>+ quantum_conductance_g0"]
    R --> C
```

#### `src/lean/SiXProofAssistant.lean` — Lean 4 proofs

```mermaid
flowchart LR
    D1["G0 := 7.748e-5"] --> T1["quantum_conductance_quantized<br/>G = channels × G0, G ≥ 0"]
    D2["calcium_update: ×0.85 + ×0.05 − extrusion"] --> T2["calcium_bounded_stability<br/>trace stays ≤ 2.5"]
    D3["Median + clip bound"] --> T3["byzantine_median_stability<br/>all weights within median ± clip"]
```

#### `src/lean/ConvexSemigroupProof.lean` — Lean 4 proofs

```mermaid
flowchart LR
    C["IsConvexCombination<br/>λ ≥ 0, Σλ = 1"] --> T1["convex_hull_bounded<br/>‖x‖ ≤ bound"]
    S["GeneratedSemigroup<br/>Σ nᵢ • pᵢ"] --> T2["semigroup_growth_unbounded<br/>(see Honest limitations)"]
```

### `ros2_nodes/` — ROS 2 edge nodes

#### `ros2_nodes/spike_bridge_node.py` — `SpikeBridgeNode`

```mermaid
flowchart LR
    S["Sensor array message"] --> CB["listener_callback"]
    CB --> ENC["Encode to spike train (torch)"]
    ENC --> OUT["Spike telemetry into mesh"]
```

#### `ros2_nodes/actuator_bridge_node.py` — `ActuatorBridgeNode`

```mermaid
flowchart LR
    C["Control command message"] --> CB["command_callback<br/>JSON parse"]
    CB --> ACT["Translate to actuator signal"]
    ACT --> OUT["Physical actuator output"]
```

#### `ros2_nodes/pathfinding_node.py` — `PathfindingBridgeNode`

```mermaid
flowchart LR
    N["Navigation / sensor message"] --> CB["navigation_callback"]
    CB --> PLAN["Neuromorphic path planning (torch)"]
    PLAN --> OUT["Path decision"]
```

### `scripts/` — ops & CI scripts

#### `scripts/ci_pipeline_workflow.sh` — the CI pipeline (run by GitHub Actions)

```mermaid
flowchart LR
    A["1/3 unittest discover<br/>tests/test_*.py"] --> B["2/3 docker compose config<br/>config/docker-compose.yml"]
    B --> C{"Lean installed?"}
    C -->|"yes"| L["3/3 lean SiXProofAssistant.lean<br/>+ ConvexSemigroupProof.lean"]
    C -->|"no"| SKIP["3/3 skip formal verification"]
    L --> PASS["CI / CD Pipeline Passed"]
    SKIP --> PASS
```

#### `scripts/run_ci_pipeline.sh` — legacy local CI

```mermaid
flowchart LR
    A["unittest discover"] --> B["docker-compose (v1) config"]
    B --> DONE["Pipeline completed"]
```

#### `scripts/deploy_mesh.sh` — deployment with CI fallbacks

```mermaid
flowchart LR
    A{"Docker Compose v2?"} -->|"yes"| B["Validate config<br/>up -d --build outside CI"]
    A -->|"no"| SKIP1["Skip container launch"]
    B --> C["HoneypotX + rclone check"]
    SKIP1 --> C
    C --> D{"CI mode?"}
    D -->|"yes"| E["py_compile ROS 2 nodes"]
    D -->|"no"| F["Launch spike + actuator bridges"]
```

#### `scripts/deploy_mesh_workflow.sh` — full deployment

```mermaid
flowchart LR
    A["docker compose up -d --build"] --> B["Activate HoneypotX + rclone sync"]
    B --> C["Start spike_bridge_node.py &"]
    C --> D["Start actuator_bridge_node.py &"]
    D --> DONE["Mesh deployed & active"]
```

#### `scripts/emergency_checkpoint_workflow.py` — `EmergencyCheckpointManager`

```mermaid
flowchart LR
    M["main: edge node state"] --> CKPT["create_tensor_checkpoint"]
    CKPT --> SYNC["sync_to_mesh via rclone"]
    SYNC --> REMOTE["secure-mesh remote"]
```

#### `scripts/generate_neural_core_assets.py` — Neural Core asset generator

```mermaid
flowchart LR
    MOD["src/neural_core_interface.py<br/>render_frame(state, phase, size, seed)"] --> HERO["5 hero frames<br/>assets/neural-core/*.png · 900×900"]
    MOD --> PHASES["20 frames<br/>4 phases × 5 states"]
    PHASES --> PAL["shared palette<br/>quantised from the IDLE hero frame"]
    PAL --> GIF["assets/neural-core.gif<br/>450 ms per frame · loops forever"]
```

### `tests/` — verification

#### `tests/test_si_x_mesh.py` — `TestSiXMesh`

```mermaid
flowchart LR
    T1["test_ani_agi_bridge<br/>64-wide experts → (2, 32)"] --> SUITE["unittest suite"]
    T2["test_error_reduced_core<br/>64-wide spikes × 32-wide valence → (2, 32)"] --> SUITE
    SUITE --> RESULT["30 tests · OK"]
```

---

## Why is this cool? — 10 reasons

- **It computes with a physical constant.** Synaptic efficacy isn't an abstract float — it's quantized into multiples of `G0 = 2e²/h`, the quantum of conductance, in three separate crossbar modules.
- **Plasticity is calcium, not just gradients.** Coincidence-driven calcium traces with `0.85` decay and homeostatic extrusion give the mesh a biologically-flavoured memory that can't saturate — and the bound is *proved in Lean*.
- **ANI and AGI in one forward pass.** Narrow experts (vision/audio/physics) are averaged and pushed through a valence-modulated general crossbar — the narrow-to-general bridge is the code, not a diagram.
- **Self-improvement with a paper trail.** Recursive mutation + evolutionary selection, but every step is versioned (`weights_version_manager`), audited (`ledger_audit_logger`), and fenced by ethics and convex-hull bounds.
- **Security is a layer, not a comment.** Gradient-poisoning clipping, a honeypot that hard-quarantines nodes, hash-chained logs, payload signing, and median consensus all ship as working modules.
- **Byzantine tolerance you can check.** Median aggregation means aberrant nodes are bounded by construction — `byzantine_median_stability` is a machine-checked theorem, not a claim.
- **It spans robot to cloud.** ROS 2 nodes on a Jetson/Pi edge topology, Redis + WebSocket + Zenoh transport, Compose/K8s/Helm manifests, and rclone checkpoint sync to any object store.
- **Hardware-aware by default.** The orchestrator routes MPS → CUDA → CPU, the stimulator emits charge-balanced biphasic pulses, and a thermal watchdog throttles before physics (Joule heating) becomes damage.
- **Formal proofs next to the code they describe.** Conductance quantization, calcium boundedness, and hull boundedness live in `src/lean/` beside the Python they model.
- **CI actually caught a real bug — and the fix is in the history.** Runs #1–3 failed on a genuine tensor-shape bug; the width-aligning fix (`a991cf25`) turned run #4 green in 2m 4s. The pipeline is a working safety net, not decoration.

---

## What problems this solves? — 10 solutions

| # | Problem | SIx solution |
|---|---|---|
| 1 | Narrow AI experts don't compose into general behaviour | `ani_agi_bridge.py` averages ANI expert encoders into one latent state and runs it through a shared AGI crossbar |
| 2 | Plastic synapses saturate and lock up over time | Calcium homeostasis (`calcium_homeostasis.py`, SERCA/NCX-style extrusion, cap 2.0) + soft trace caps in every crossbar; boundedness proved in Lean |
| 3 | Mixed-width tensors crash neuromorphic pipelines (the CI #1–3 bug) | `error_reduction_mesh.py` aligns *any* input width onto `out_features` before combining — verified by `test_error_reduced_core` |
| 4 | Poisoned gradients from a compromised node corrupt the whole mesh | `adversarial_defense.py` clips any gradient tensor whose norm exceeds 12.0 |
| 5 | One lying/faulty node drags federated aggregation off course | Median consensus (`consensus_validator.py`, `federated_synaptic_aggregation`) — aberrant updates are bounded by the median ± clip theorem |
| 6 | No audit trail when an autonomous system misbehaves | `ledger_audit_logger.py` hash-chains every state transition and safety violation from a genesis block |
| 7 | Edge nodes die and lose learned state | Emergency checkpoints (`emergency_checkpoint_workflow.py`, `multicloud_sync.py`) rclone-sync tensor state to `secure-mesh:checkpoints/si-x/` every 300 s and on breach |
| 8 | Sensor drift poisons downstream decisions | Extended Kalman filtering (`ekf_sensory_bridge.py`) and SAR speckle filtering (`sar_fusion_node.py`) clean signals before fusion |
| 9 | Self-modifying systems drift out of bounds | Ethical goal filtering (`ethical_goal_automation.py`), convex-hull containment (`convex_hull_semigroup_mesh.py`), thermal throttling (`thermal_watchdog.py`), and versioned rollback (`weights_version_manager.py`) |
| 10 | Telemetry chaos across robots, edge boxes, and cloud | One transport story: Redis pub/sub + WebSocket streaming + Zenoh peer config, with payload signing (`pq_crypto_bridge.py`) and fleet-level consensus (`fleet_telemetry_aggregator.py`) |

---

## How to install this — step by step

> You only need **Python + PyTorch** to run the verified test suite. ROS 2, Docker, Redis, and Lean are needed only for the layers that use them (see Requirements).

- **Clone the repo**
   ```bash
   git clone https://github.com/kimanicollier44-cmyk/SIx.git
   cd SIx
   ```
- **Create a virtual environment (Python 3.12)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```
- **Install the requirements**
   ```bash
   pip install -r requirements.txt
   ```
   This installs `torch>=2.0.0` and `pytest`. On a CPU-only machine, the CPU wheel is enough:
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cpu
   ```
- **Run the test suite — the same command CI runs**
   ```bash
   python3 -m unittest discover -s tests -p "test_*.py"
   ```
   Expected: `Ran 30 tests ... OK`
- **(Optional) Run the full CI script locally**
   ```bash
   chmod +x scripts/ci_pipeline_workflow.sh
   ./scripts/ci_pipeline_workflow.sh
   ```
   Step 2 needs Docker Compose v2 (`docker compose config`); step 3 checks the Lean proofs only if `lean` is on your PATH, and skips cleanly otherwise.
- **(Optional) Validate / launch the Compose stack**
   ```bash
   docker compose -f config/docker-compose.yml config   # validate only
   docker compose -f config/docker-compose.yml up --build
   ```
   See Honest limitations before expecting the `si-x-fastapi` service to serve — the repo ships no Dockerfile yet.
- **(Optional) Run the ROS 2 edge nodes** — needs a ROS 2 install (`rclpy`, `std_msgs`) on the edge box:
   ```bash
   python3 ros2_nodes/spike_bridge_node.py
   python3 ros2_nodes/actuator_bridge_node.py
   ```
- **(Optional) Start the WebSocket telemetry streamer** — needs the `websockets` package:
   ```bash
   pip install websockets
   python3 src/websocket_streamer.py   # ws://0.0.0.0:8765
   ```
- **(Optional) Configure the watchdog + sync** — edit `config/security-watchdog.conf` (thresholds, rclone remote `secure-mesh:checkpoints/si-x/`, 65 °C thermal limit) and configure that rclone remote before running `scripts/deploy_mesh.sh` or `scripts/emergency_checkpoint_workflow.py`.

---

## Requirements

**Required for the verified core (tests + CI):**

| Requirement | Version / note |
|---|---|
| Python | 3.12 (CI-pinned; modules are plain PyTorch and also run on nearby 3.x) |
| PyTorch | `torch>=2.0.0` — in `requirements.txt`; CPU wheel is sufficient for the tests |
| pytest | In `requirements.txt` (the suite itself is `unittest`-style and runs without pytest) |
| Bash | For `scripts/*.sh` |
| Docker Compose v2 | Only for CI step 2 / the Compose stack (`docker compose config`) |

**Optional — only for the layer that uses it (NOT in `requirements.txt`):**

| Requirement | Used by |
|---|---|
| ROS 2 (`rclpy`, `std_msgs`) | `ros2_nodes/*.py` |
| `redis` Python client + a Redis server | `src/redis_pubsub_bridge.py` (server: `redis:alpine` in Compose) |
| `websockets` | `src/websocket_streamer.py` |
| FastAPI + Uvicorn | The `si-x-fastapi` Compose service command |
| Lean 4 + Mathlib | `src/lean/*.lean` (CI skips this step when Lean is absent) |
| rclone + a configured `secure-mesh` remote | `src/multicloud_sync.py`, `scripts/emergency_checkpoint_workflow.py` |
| NVIDIA Jetson Orin Nano / Raspberry Pi 5 + Hailo-8 / Apple Silicon | The edge topology and MPS bridge — the code runs on plain CPU without them |

---

## 📂 FULL project structure tree

```
SIx/
├── README.md
├── requirements.txt
├── .github/workflows/
│   ├── ci_pipeline_workflow.sh
│   ├── si_x_pipeline.yml
├── config/
│   ├── docker-compose.yml
│   ├── edge-topology.yaml
│   ├── k8s-ingress.yaml
│   ├── security-watchdog.conf
│   ├── zenoh-tcp.json
├── config/helm/
│   ├── Chart.yaml
├── ros2_nodes/
│   ├── actuator_bridge_node.py
│   ├── pathfinding_node.py
│   ├── spike_bridge_node.py
├── scripts/
│   ├── __init__.py
│   ├── ci_pipeline_workflow.sh
│   ├── deploy_mesh.sh
│   ├── deploy_mesh_workflow.sh
│   ├── emergency_checkpoint_workflow.py
│   ├── generate_neural_core_assets.py
│   ├── run_ci_pipeline.sh
├── src/
│   ├── __init__.py
│   ├── adversarial_defense.py
│   ├── ani_agi_bridge.py
│   ├── biphasic_stimulator.py
│   ├── calcium_homeostasis.py
│   ├── consensus_validator.py
│   ├── continuous_meta_learner.py
│   ├── convex_hull_semigroup_mesh.py
│   ├── creative_generative_engine.py
│   ├── docker_fleet_registry.py
│   ├── ekf_sensory_bridge.py
│   ├── error_reduction_mesh.py
│   ├── ethical_goal_automation.py
│   ├── evolutionary_neuromorphic_core.py
│   ├── federated_curriculum.py
│   ├── fleet_telemetry_aggregator.py
│   ├── honeypot_mission_guard.py
│   ├── industry_4_mesh.py
│   ├── ledger_audit_logger.py
│   ├── memory_buffer_manager.py
│   ├── mesh_orchestrator.py
│   ├── mission_planner.py
│   ├── multi_agent_negotiation.py
│   ├── multi_sensory_fusion_core.py
│   ├── multicloud_sync.py
│   ├── nanoscale_matrix.py
│   ├── neural_core_interface.py
│   ├── osx_native_bridge.py
│   ├── pq_crypto_bridge.py
│   ├── quantum_conductance.py
│   ├── quantum_neural_cryptography.py
│   ├── recursive_self_improvement.py
│   ├── redis_pubsub_bridge.py
│   ├── sar_fusion_node.py
│   ├── snn_codec.py
│   ├── system_diagnostic_dashboard.py
│   ├── thermal_watchdog.py
│   ├── unified_mesh_orchestrator.py
│   ├── valence_memory_controller.py
│   ├── websocket_streamer.py
│   ├── weights_version_manager.py
├── src/lean/
│   ├── ConvexSemigroupProof.lean
│   ├── SiXProofAssistant.lean
├── tests/
│   ├── test_docker_fleet_registry.py
│   ├── test_neural_core_interface.py
│   ├── test_si_x_mesh.py
├── assets/
│   ├── neural-core.gif
│   ├── neural-core/
│   │   ├── idle.png
│   │   ├── learning.png
│   │   ├── listening.png
│   │   ├── responding.png
│   │   ├── thinking.png
```

72 files total. (`assets/cover.png` is added by uploading the cover image to an `assets/` folder — the README header points there. The Neural Core GIF and state frames under `assets/` are generated by `scripts/generate_neural_core_assets.py`.)

---

## ✅ Verification status

- **GitHub Actions run #4** for head `a991cf25` — **SUCCESS, 2m 4s** (2026-11-17): unittest suite, Docker Compose config validation, Lean step skipped (no Lean on the runner).
- **Runs #1–3 failed** on the `error_reduction_mesh` tensor-shape bug described above; the fix is commit `a991cf25`.
- **Local verification of that fix:** unittest 2/2 OK (CPU torch) at the time — the suite has since grown to **30/30 OK** across 3 test modules (mesh 2, fleet registry 11, Neural Core 17; CPU torch) — plus width-combination checks (64×32, 64×64, 32×32, single-tensor) all returning the correct output shape, and `docker compose config` exit 0.
- **Every badge URL in this README was checked live** before this README was pushed. The workflow badge is the live Shields Actions-status badge for `si_x_pipeline.yml` on `main`.
- **PUSHED:** kimanicollier44-cmyk/SIx, head **11daa162** — fleet Docker registry merged (registry module, aggregator wiring, 11 registry tests, this README); all 4 read-back blobs = local.

## ⚠️ Honest limitations

- **Simulated hardware.** Memristor crossbars, quantum conductance, biphasic stimulation, and thermal behaviour are software models. No physical device is driven by this code as shipped.
- **Cryptography is a model.** `pq_crypto_bridge.py` and `quantum_neural_cryptography.py` are lattice-*inspired* hashing / oscillator simulations built on `hashlib` — not audited, certified post-quantum cryptography. Don't secure real traffic with them.
- **No Dockerfile yet.** `config/docker-compose.yml` declares `build: .` for `si-x-fastapi` and `scout-bot-agent`, but the repo contains no Dockerfile, and `src/mesh_orchestrator.py` defines `ZeroShotAGICrossbar`, not a FastAPI `app` object — so `docker compose config` validates, but `up --build` will not serve until a Dockerfile and an `app` entrypoint are added.
- **Optional deps aren't in `requirements.txt`.** `redis`, `websockets`, `rclpy`, FastAPI/Uvicorn are imported by their modules but must be installed separately (see Requirements).
- **One Lean proof is incomplete.** `semigroup_growth_unbounded` in `src/lean/ConvexSemigroupProof.lean` ends in `sorry`. The other theorems (conductance quantization, calcium boundedness, Byzantine median stability, convex-hull boundedness) are complete as written; Lean is not installed on the CI runner, so CI does not type-check these files.
- **A stray shell script lives in `.github/workflows/`.** `.github/workflows/ci_pipeline_workflow.sh` is a duplicate of the CI script; GitHub Actions ignores non-YAML files there. The real pipeline script is `scripts/ci_pipeline_workflow.sh`, and the legacy `scripts/run_ci_pipeline.sh` still calls Compose v1 (`docker-compose`).
- **Test coverage is still uneven.** 30 unit tests cover the ANI→AGI bridge and the error-reduction core (2), the Docker fleet registry (11), and the Neural Core interface (17). The other 36 `src/` modules are exercised only by import in this README's audit, not by dedicated tests.

---

*SIx (Gen-Intel Secure Mesh) — by Darion Kellar / kimanicollier44-cmyk. Research architecture: simulated neuromorphic mesh, formal proofs, and a CI pipeline that earned its green check.*
