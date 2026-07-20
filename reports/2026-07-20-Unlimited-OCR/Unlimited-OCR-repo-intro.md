# baidu/Unlimited-OCR 仓库介绍

更新时间：2026-07-19  
仓库地址：https://github.com/baidu/Unlimited-OCR

## 1. 仓库一句话概括

`baidu/Unlimited-OCR` 是百度发布的 Unlimited-OCR 模型仓库配套代码与文档。它的目标不是做一个传统 OCR 桌面软件，而是提供一个面向长文档、长上下文、多页图片或 PDF 的端到端文档解析模型。

仓库 README 给出的核心口号是：

> Welcome the Era of One-shot Long-horizon Parsing.

也就是说，它强调“一次性长程解析”：把多页文档或长图片内容交给视觉语言模型，直接生成结构化文本或 Markdown 式 OCR 结果。

## 2. 它主要解决什么问题

传统 OCR 流程通常会拆成多个阶段：

1. 文本检测
2. 文本识别
3. 版面分析
4. 表格、公式、段落结构恢复
5. 多页结果拼接

Unlimited-OCR 更接近视觉语言模型路线：输入图片或 PDF 页面后，由模型直接生成文档解析结果。它特别关注长文档场景，希望减少逐页解析、再后处理拼接带来的信息断裂。

适合的任务包括：

- 扫描件 OCR
- 多页 PDF 文档解析
- 长图文档解析
- 表格、段落、标题、公式等结构化内容恢复
- 将文档图片转换为 Markdown 或较规整的文本
- 研究长上下文 OCR、视觉语言模型文档理解、KV cache 优化等方向

不太适合的场景：

- 只需要轻量级本地 OCR 工具
- 没有 NVIDIA GPU 的本地环境
- 需要传统 OCR 引擎输出字符框、检测框、置信度等细粒度结构
- 不希望在生产环境中使用 `trust_remote_code=True`

## 3. 仓库内容结构

这个 GitHub 仓库本身比较轻，更像“论文 + 模型发布 + 推理示例”的工程入口。主要文件包括：

| 文件或目录 | 作用 |
| --- | --- |
| `README.md` | 项目说明、发布记录、Transformers/vLLM/SGLang 推理方式 |
| `infer.py` | 基于 SGLang 的并发推理脚本，支持图片目录和 PDF |
| `Unlimited-OCR.pdf` | 论文 PDF |
| `wheel/` | README 中提到的本地 SGLang wheel |
| `assets/` | README 展示图、logo、动图等 |
| `LICENSE` | MIT 开源协议 |
| `CONTRIBUTING.md` | 贡献规范 |

需要注意：真正的模型权重和自定义模型代码不完全放在 GitHub 仓库里，而是在 Hugging Face 模型仓库中：

https://huggingface.co/baidu/Unlimited-OCR

通过 Transformers 加载时，需要使用：

```python
trust_remote_code=True
```

这说明模型实现依赖 Hugging Face 端的自定义 Python 代码。

## 4. 发布状态

README 中列出的发布时间线：

- 2026-06-22：发布 Unlimited-OCR，目标是进一步推进 DeepSeek-OCR 方向。
- 2026-06-23：论文上线 arXiv。
- 2026-06-23：模型上线 ModelScope。
- 2026-06-24：上线 Hugging Face Spaces Demo。
- 2026-06-28：支持 vLLM 推理。
- 2026-07-03：模型上线百度智能云。

相关入口：

- GitHub：https://github.com/baidu/Unlimited-OCR
- Hugging Face：https://huggingface.co/baidu/Unlimited-OCR
- arXiv：https://arxiv.org/abs/2606.23050
- ModelScope：https://modelscope.cn/models/PaddlePaddle/Unlimited-OCR
- Hugging Face Spaces：https://huggingface.co/spaces/baidu/Unlimited-OCR
- 百度智能云文档：https://cloud.baidu.com/doc/OCR/s/fmr1p39gb

## 5. 核心技术思路

从公开文档看，Unlimited-OCR 属于视觉语言模型式 OCR。它不是只做字符识别，而是让模型直接读图并生成文档解析结果。

大致链路可以理解为：

```text
图片或 PDF
  -> PDF 页面转图片
  -> 图像编码器提取视觉特征
  -> 视觉特征映射到语言模型可接收的 embedding
  -> 语言模型 decoder 生成 OCR/Markdown 文本
  -> 保存为解析结果文件
```

论文强调的关键点是长程解析能力。它提出 Reference Sliding Window Attention，也就是 R-SWA，用来降低长序列解码时 KV cache 的增长压力。直观理解是：模型在处理长文档输出时，不希望所有历史 token 都无限制保留完整注意力缓存，而是通过滑动窗口和参考机制控制缓存规模，使长上下文解析更可行。

README 中的最大长度示例是：

```python
max_length=32768
```

这说明官方示例默认面向 32K 级别的长输出。

## 6. 支持的推理方式

仓库 README 给了三种推理路线。

### 6.1 Transformers

这是最直接的 Python 加载方式，适合调试和研究。

核心加载方式：

```python
from transformers import AutoModel, AutoTokenizer

model_name = "baidu/Unlimited-OCR"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModel.from_pretrained(
    model_name,
    trust_remote_code=True,
    use_safetensors=True,
    torch_dtype=torch.bfloat16,
)
model = model.eval().cuda()
```

官方测试环境：

```text
Python 3.12.3
CUDA 12.9
torch==2.10.0
torchvision==0.25.0
transformers==4.57.1
Pillow==12.1.1
matplotlib==3.10.8
einops==0.8.2
addict==2.4.0
easydict==1.13
pymupdf==1.27.2.2
psutil==7.2.2
```

### 6.2 vLLM

README 说明模型已经支持 vLLM 推理，并给出官方 recipe：

https://recipes.vllm.ai/baidu/Unlimited-OCR

Docker 镜像：

```bash
docker pull vllm/vllm-openai:unlimited-ocr
```

Hopper GPU / CUDA 12.9 镜像：

```bash
docker pull vllm/vllm-openai:unlimited-ocr-cu129
```

这一路线适合做服务化部署。

### 6.3 SGLang

GitHub 仓库里的 `infer.py` 主要围绕 SGLang 并发推理。

README 给出的服务启动方式类似：

```bash
python -m sglang.launch_server \
    --model baidu/Unlimited-OCR \
    --served-model-name Unlimited-OCR \
    --attention-backend fa3 \
    --page-size 1 \
    --mem-fraction-static 0.8 \
    --context-length 32768 \
    --enable-custom-logit-processor \
    --disable-overlap-schedule \
    --skip-server-warmup \
    --host 0.0.0.0 \
    --port 10000
```

然后通过 OpenAI-compatible API 发送请求：

```text
POST http://127.0.0.1:10000/v1/chat/completions
```

## 7. `infer.py` 做了什么

`infer.py` 是仓库里最关键的脚本。它的作用是自动启动 SGLang server，并对图片目录或 PDF 页面做并发 OCR 请求。

它支持两种输入模式：

1. 图片目录：传入 `--image_dir`，目录下每张图片作为一个请求。
2. PDF：传入 `--pdf`，脚本用 PyMuPDF 把 PDF 每一页转成图片，再逐页请求模型。

典型命令：

```bash
python infer.py \
    --image_dir ./examples/images \
    --output_dir ./outputs \
    --concurrency 8 \
    --image_mode gundam
```

```bash
python infer.py \
    --pdf ./examples/document.pdf \
    --output_dir ./outputs \
    --concurrency 8 \
    --image_mode gundam
```

常用参数：

| 参数 | 含义 |
| --- | --- |
| `--image_dir` | 图片目录输入 |
| `--pdf` | PDF 文件输入 |
| `--output_dir` | 输出目录，默认 `./outputs` |
| `--concurrency` | 并发请求数，默认 8 |
| `--gpu` | 设置 `CUDA_VISIBLE_DEVICES`，默认 `0` |
| `--model_dir` | 模型路径或 Hugging Face 模型 ID，默认 `baidu/Unlimited-OCR` |
| `--image_mode` | 图像模式，可选 `gundam` 或 `base` |
| `--server_log` | SGLang server 日志路径 |

脚本内部做的事情：

1. 检查 `http://127.0.0.1:10000/health` 是否已有可用 SGLang server。
2. 如果没有，则通过 `subprocess.Popen` 启动 `sglang.launch_server`。
3. 如果输入是 PDF，则用 PyMuPDF 按 300 DPI 转成临时图片。
4. 将图片转成 base64 data URL。
5. 构造 OpenAI-compatible chat completions 请求。
6. 使用 streaming 接收模型输出。
7. 把每张图片或每页 PDF 的结果写成 `.md` 文件。
8. 输出总 token 数、耗时、系统 TPS、平均 token 数等统计信息。

## 8. 图像模式：gundam 和 base

README 中提到单图支持两套配置：

```text
gundam: base_size=1024, image_size=640, crop_mode=True
base:   base_size=1024, image_size=1024, crop_mode=False
```

多页或 PDF 场景 README 的 Transformers 示例说明使用 base 模式：

```python
model.infer_multi(..., image_size=1024, ...)
```

但 `infer.py` 的默认值是：

```python
parser.add_argument("--image_mode", choices=("gundam", "base"), default="gundam")
```

所以实际使用时需要根据后端和任务类型实测。稳妥做法是：

- 单图 OCR：先试 `gundam`。
- 多页或 PDF：优先试 `base`，再对比 `gundam` 的效果和性能。

## 9. 输出结果形态

`infer.py` 默认把输出保存到 `./outputs` 目录。

图片目录模式下，输出文件名来自图片相对路径，例如：

```text
outputs/page_001.md
outputs/subdir__image_002.md
```

PDF 模式下，输出文件名类似：

```text
outputs/document_page_0001.md
outputs/document_page_0002.md
```

这说明它的默认批处理脚本是“每张图或每页 PDF 输出一个 Markdown 文件”。如果要做完整文档级后处理，还需要额外把多页结果合并、排序、清洗和校验。

## 10. 工程成熟度判断

这个仓库更像模型发布仓库，不是完整产品工程。

优点：

- 文档给出了 Transformers、vLLM、SGLang 三种推理方式。
- 有批量并发推理脚本 `infer.py`。
- 支持图片目录和 PDF。
- 使用 MIT 协议，二次开发约束较少。
- 已提供 Hugging Face、ModelScope、Baidu Cloud 等入口。

限制：

- GitHub 仓库本身代码较少。
- 没有完整 Python package 结构。
- 没有专门的测试目录。
- 生产部署需要自己处理环境、GPU、服务稳定性、结果后处理和安全审查。
- Transformers 路线依赖 `trust_remote_code=True`，上线前需要审查 Hugging Face 模型代码。
- 官方依赖版本较新，对 CUDA、PyTorch、Transformers 版本比较敏感。

## 11. 本地部署注意事项

如果要在本地尝试，建议先确认：

1. 是否有 NVIDIA GPU。
2. CUDA 版本是否匹配。
3. Python 是否为 3.12 左右。
4. 是否可以接受下载约数 GB 级模型权重。
5. 是否能使用 `trust_remote_code=True`。
6. 是否使用 vLLM/SGLang 这类高性能推理框架。

如果只是想体验效果，优先使用 Hugging Face Spaces 或百度智能云入口，成本更低。

如果要二次开发，建议优先走 SGLang 或 vLLM 服务化路线，而不是直接把 Transformers 示例包装成生产服务。

## 12. 推荐阅读顺序

1. 先读 GitHub README，了解发布信息和官方推理方式。
2. 再读 `infer.py`，理解官方批量并发推理脚本。
3. 再看 Hugging Face 模型仓库，确认模型配置、权重和 remote code。
4. 如果关心原理，读 arXiv 论文，重点看 R-SWA 和长文档解析部分。
5. 如果要部署服务，优先看 vLLM recipe 或 SGLang 启动参数。

## 13. 总结

`baidu/Unlimited-OCR` 的核心价值是长文档 OCR 和一次性多页解析。它不是传统 OCR 工具链，而是视觉语言模型式的文档解析模型发布仓库。

它适合研究和搭建高能力 OCR 服务，尤其是多页 PDF、扫描件、长图、结构化文档解析等场景。真正落地时，需要关注 GPU 环境、推理框架、模型代码安全、输出后处理和多页结果合并。

对于开发者来说，最值得看的代码是 `infer.py`；最值得理解的机制是 R-SWA；最值得验证的工程路径是 vLLM 或 SGLang 服务化推理。
