#!/usr/bin/env python3
"""
Story Structure Helper - Công cụ xây dựng cấu trúc câu chuyện

Usage:
    python structure_helper.py --model three_act --genre fairytale
    python structure_helper.py --model hero_journey --theme adventure --output structure.md
    python structure_helper.py --model circular --format json
"""

import argparse
import json
from typing import Dict, List, Any

class StoryStructureHelper:
    def __init__(self):
        self.structure_models = self._load_structure_models()
        self.genre_modifiers = self._load_genre_modifiers()
        self.theme_elements = self._load_theme_elements()
        
    def _load_structure_models(self) -> Dict[str, Dict[str, Any]]:
        """Load different story structure models"""
        return {
            "three_act": {
                "name": "Cấu trúc 3 hồi",
                "description": "Cấu trúc kinh điển với mở đầu, cao trào, và kết thúc",
                "acts": [
                    {
                        "name": "Hồi 1: Thiết lập",
                        "percentage": 25,
                        "elements": [
                            "Giới thiệu nhân vật chính và thế giới",
                            "Xác định mục tiêu hoặc mong muốn của nhân vật",
                            "Thiết lập trạng thái bình thường",
                            "Giới thiệu vấn đề hoặc cơ hội đầu tiên"
                        ],
                        "questions": [
                            "Nhân vật chính là ai và đang sống ở đâu?",
                            "Điều gì quan trọng nhất với nhân vật này?",
                            "Sự kiện nào đã phá vỡ cuộc sống bình thường?"
                        ]
                    },
                    {
                        "name": "Hồi 2: Xung đột phát triển",
                        "percentage": 50,
                        "elements": [
                            "Nhân vật chấp nhận thử thách",
                            "Gặp phải khó khăn và đối đầu",
                            "Sự leo thang của xung đột",
                            "Thất bại nhỏ và thành công lớn xen kẽ",
                            "Điểm quay vòng (midpoint) thay đổi mọi thứ"
                        ],
                        "questions": [
                            "Nhân vật đã làm gì để giải quyết vấn đề?",
                            "Điều gì đã cản trở nhân vật?",
                            "Sự kiện nào đã thay đổi hoàn toàn tình thế?"
                        ]
                    },
                    {
                        "name": "Hồi 3: Giải quyết",
                        "percentage": 25,
                        "elements": [
                            "Đỉnh điểm của xung đột",
                            "Nhân vật đối mặt với thử thách cuối cùng",
                            "Giải quyết vấn đề chính",
                            "Kết quả và bài học",
                            "Trở lại trạng thái mới ổn định"
                        ],
                        "questions": [
                            "Nhân vật phải đối mặt với thử thách lớn nhất nào?",
                            "Nhân vật đã giải quyết vấn đề như thế nào?",
                            "Nhân vật đã trở thành người như thế nào sau câu chuyện?"
                        ]
                    }
                ]
            },
            
            "hero_journey": {
                "name": "Hành trình của người hùng",
                "description": "Cấu trúc 12 bước cho cuộc phiêu lưu hoành tráng",
                "stages": [
                    {
                        "phase": "PhÁN 1: Ra đi",
                        "steps": [
                            {
                                "name": "Thế giới bình thường",
                                "description": "Nhân vật sống trong cuộc đời thường, biết đến sự tồn tại của thế giới phi thường"
                            },
                            {
                                "name": "Lời kêu gọi phiêu lưu",
                                "description": "Một sự kiện xảy ra, phá vỡ thế giới bình thường và kêu gọi nhân vật hành động"
                            },
                            {
                                "name": "Từ chối lời kêu gọi",
                                "description": "Nhân vật ngần ngại hoặc sợ hãi, ban đầu từ chối cuộc phiêu lưu"
                            },
                            {
                                "name": "Gặp người hướng dẫn",
                                "description": "Nhân vật gặp người thầy hoặc người hướng dẫn đưa ra sự giúp đỡ hoặc kiến thức"
                            },
                            {
                                "name": "Vượt qua ngưỡng cửa đầu tiên",
                                "description": "Nhân vật quyết tâm và bước vào thế giới phi thường"
                            }
                        ]
                    },
                    {
                        "phase": "PHÁN 2: Thử thách",
                        "steps": [
                            {
                                "name": "Thử nghiệm, đồng minh và kẻ thù",
                                "description": "Nhân vật học quy tắc của thế giới mới, tìm ra đồng minh và kẻ thù"
                            },
                            {
                                "name": "Tiến vào hang ổ sâu nhất",
                                "description": "Nhân vật chuẩn bị đối mặt với thử thách lớn nhất"
                            },
                            {
                                "name": "Thử thách tối thượng",
                                "description": "Khoảnh khắc khó khăn nhất, đối mặt với cái chết hoặc thất bại"
                            },
                            {
                                "name": "Phần thưởng",
                                "description": "Nhân vật đạt được mục tiêu, tìm thấy kiến thức hay vật phẩm quý giá"
                            }
                        ]
                    },
                    {
                        "phase": "PHÁN 3: Trở về",
                        "steps": [
                            {
                                "name": "Con đường trở về",
                                "description": "Nhân vật quyết định trở về thế giới bình thường"
                            },
                            {
                                "name": "Phục sinh",
                                "description": "Thử thách cuối cùng, nhân vật được làm lại và thử nghiệm một lần nữa"
                            },
                            {
                                "name": "Trở về với phép màu",
                                "description": "Nhân vật trở về nhà với phần thưởng hoặc kiến thức"
                            }
                        ]
                    }
                ]
            },
            
            "fable_structure": {
                "name": "Cấu trúc truyện ngụ ngôn",
                "description": "Cấu trúc đơn giản cho truyện ngụ ngôn có bài học",
                "sections": [
                    {
                        "name": "Giới thiệu",
                        "percentage": 15,
                        "content": [
                            "Giới thiệu loài vật và đặc tính của chúng",
                            "Thiết lập bối cảnh (khu rừng, đồng cỏ, sông, hồ)",
                            "Đề xuất phẩm chất hoặc thói quen chính của nhân vật"
                        ]
                    },
                    {
                        "name": "Phát triển tình huống",
                        "percentage": 25,
                        "content": [
                            "Tạo ra tình huống thử thách phẩm chất ban đầu",
                            "Nhân vật chính đưa ra lựa chọn",
                            "Gặp nhân vật thứ hai (nếu có)"
                        ]
                    },
                    {
                        "name": "Xung đột",
                        "percentage": 35,
                        "content": [
                            "Hậu quả của lựa chọn ban đầu",
                            "Tương tác giữa các nhân vật",
                            "Leo thang vấn đề",
                            "Điểm quyết định"
                        ]
                    },
                    {
                        "name": "Giải quyết và bài học",
                        "percentage": 25,
                        "content": [
                            "Kết quả cuối cùng",
                            "Hành động sửa chữa hoặc học hỏi",
                            "Bài học đạo đức rõ ràng",
                            "Thông điệp kết thúc"
                        ]
                    }
                ]
            },
            
            "circular": {
                "name": "Cấu trúc vòng tròn",
                "description": "Cấu trúc bắt đầu và kết thúc ở cùng một điểm nhưng với sự thay đổi",
                "phases": [
                    {
                        "name": "Trạng thái ban đầu",
                        "description": "Giới thiệu tình huống và vấn đề hiện tại"
                    },
                    {
                        "name": "Thử thách xuất hiện",
                        "description": "Sự kiện thay đổi bắt đầu chuỗi biến đổi"
                    },
                    {
                        "name": "Thử nghiệm và thất bại",
                        "description": "Nhân vật vượt qua thử thách, học từ thất bại"
                    },
                    {
                        "name": "Thấu hiểu và thay đổi",
                        "description": "Nhân vật nhận ra sự thật về bản thân hoặc thế giới"
                    },
                    {
                        "name": "Trở lại điểm ban đầu",
                        "description": "Quay lại tình huống ban đầu nhưng với góc nhìn và khả năng mới"
                    }
                ]
            }
        }
    
    def _load_genre_modifiers(self) -> Dict[str, List[str]]:
        """Load genre-specific structure modifications"""
        return {
            "fairytale": [
                "Bắt đầu với 'Ngày xửa ngày xưa' hoặc tương tự",
                "Phép thuật và sự kiện siêu nhiên",
                "Nhân vật rõ ràng: tốt hoặc xấu",
                "Bài học đạo đức ở cuối",
                "Kết thúc hạnh phúc ('sống hạnh phúc mãi mãi')"
            ],
            "fable": [
                "Nhân vật là động vật hóa thân",
                "Một phẩm chất chính được thể hiện",
                "Tình huống đơn giản, dễ hiểu",
                "Bài học trực tiếp và rõ ràng",
                "Kết thúc với thông điệp đạo đức"
            ],
            "children": [
                "Ngôn ngữ đơn giản, phù hợp độ tuổi",
                "Nhân vật gần gũi với trẻ em",
                "Cốt truyện dễ theo dõi",
                "Thông điệp tích cực về tình bạn, lòng tốt, dũng cảm",
                "Kết thúc vui vẻ và đầy hy vọng"
            ],
            "adventure": [
                "Hành trình đến những nơi xa lạ",
                    "Thử thách ngày càng khó khăn",
                    "Phát hiện và khám phá",
                    "Phát triển nhân vật qua thử thách",
                    "Phần thưởng và thành công"
            ]
        }
    
    def _load_theme_elements(self) -> Dict[str, List[str]]:
        """Load theme-specific structural elements"""
        return {
            "friendship": [
                "Giới thiệu về tình bạn ban đầu",
                "Kiểm tra tình bạn qua thử thách",
                "Sự phản bội hoặc hiểu lầm",
                "Hối lỗi và tha thứ",
                "Tình bạn được củng cố mạnh mẽ hơn"
            ],
            "honesty": [
                "Tình huống考验 sự trung thực",
                "Dối trá có vẻ mang lợi ích ngắn hạn",
                "Hậu quả của sự không trung thực",
                "Sự thật được phơi bày",
                " học học học học học học học học học học value of truth"
            ],
            "courage": [
                "Nỗi sợ hãi ban đầu",
                "Bắt buộc phải đối mặt",
                "Thử thách vượt qua sợ hãi",
                "Phát hiện lòng can đảm nội tại",
                "Trở thành người dũng cảm"
            ],
            "kindness": [
                "Hiện tại sự bất nhân",
                "Cơ hội thể hiện lòng tốt",
                "Lòng tốt bị từ chối hoặc đánh giá thấp",
                "Lòng tốt cuối cùng được ghi nhận",
                "Thế giới trở nên tốt đẹp hơn"
            ]
        }
    
    def generate_structure(self, model: str, genre: str = None, 
                          theme: str = None, format_type: str = "markdown") -> Dict[str, Any]:
        """Generate story structure based on parameters"""
        
        if model not in self.structure_models:
            raise ValueError(f"Unknown structure model: {model}")
        
        structure = self.structure_models[model].copy()
        
        # Add genre modifications
        if genre:
            structure["genre_modifiers"] = self.genre_modifiers.get(genre, [])
            structure["genre"] = genre
        
        # Add theme elements
        if theme:
            structure["theme_elements"] = self.theme_elements.get(theme, [])
            structure["theme"] = theme
        
        # Generate step-by-step outline
        if model == "three_act":
            outline = self._generate_three_act_outline(structure, genre, theme)
        elif model == "hero_journey":
            outline = self._generate_hero_journey_outline(structure, genre, theme)
        elif model == "fable_structure":
            outline = self._generate_fable_outline(structure, genre, theme)
        elif model == "circular":
            outline = self._generate_circular_outline(structure, genre, theme)
        else:
            outline = {"error": "Unknown model"}
        
        structure["outline"] = outline
        
        return structure
    
    def _generate_three_act_outline(self, structure: Dict, genre: str, theme: str) -> Dict:
        """Generate specific outline for three-act structure"""
        outline = {
            "act_1": {
                "title": "Hồi 1: Thiết lập (25%)",
                "steps": [
                    "1. Giới thiệu nhân vật chính và cuộc sống bình thường",
                    "2. Thiết lập mục tiêu mong muốn của nhân vật", 
                    "3. Sự kiện kích hoạt phá vỡ bình thường",
                    "4. Nhân vật đối mặt với lựa chọn chấp nhận hay từ chối"
                ]
            },
            "act_2": {
                "title": "Hồi 2: Xung đột (50%)",
                "steps": [
                    "1. Nhân vật bước vào thế giới mới, gặp thử thách đầu tiên",
                    "2. Tìm kiếm đồng minh và đối mặt với kẻ thù",
                    "3. Leo thang khó khăn, thất bại nhỏ và học hỏi",
                    "4. Điểm quay vòng: sự kiện thay đổi hoàn toàn tình thế",
                    "5. Chuẩn bị cho đối đầu cuối cùng"
                ]
            },
            "act_3": {
                "title": "Hồi 3: Giải quyết (25%)",
                "steps": [
                    "1. Đỉnh điểm: đối mặt với thử thách lớn nhất",
                    "2. Giải quyết vấn đề chính",
                    "3. Hậu quả và kết quả",
                    "4. Nhân vật trưởng thành và thay đổi",
                    "5. Trở lại trạng thái cân bằng mới"
                ]
            }
        }
        
        # Add genre-specific notes
        if genre == "fairytale":
            outline["genre_notes"] = [
                "Bắt đầu với cổ tích mở đầu chuẩn",
                "Giới thiệu phép thuật vào hồi 2",
                "Kết thúc với đám cưới hoặc 'sống hạnh phúc'"
            ]
        elif genre == "fable":
            outline["genre_notes"] = [
                "Tập trung vào một phẩm chất chính",
                "Tình huống đơn giản làm nổi bật bài học",
                "Kết thúc rõ ràng với thông điệp"
            ]
        
        return outline
    
    def _generate_hero_journey_outline(self, structure: Dict, genre: str, theme: str) -> Dict:
        """Generate specific outline for hero's journey"""
        heroine_journey_stages = self.structure_models["hero_journey"]["stages"]
        
        outline = {
            "phase_1": {
                "title": "PhÁN 1: Ra đi",
                "steps": [
                    "1. Thế giới bình thường: giới thiệu cuộc sống thường ngày",
                    "2. Lời kêu gọi phiêu lưu: sự kiện phá vỡ bình thường",
                    "3. Từ chối lời kêu gọi: ngần ngại và sợ hãi",
                    "4. Gặp người hướng dẫn: giúp đỡ và sự chuẩn bị",
                    "5. Vượt ngưỡng cửa: quyết định tham gia phiêu lưu"
                ]
            },
            "phase_2": {
                "title": "PHÁN 2: Thử thách và biến đổi",
                "steps": [
                    "6. Thử nghiệm, đồng minh và kẻ thù: học quy tắc thế giới mới",
                    "7. Tiến vào hang ổ sâu nhất: chuẩn bị đối mặt thử thách lớn",
                    "8. Thử thách tối thượng: đối mặt thất bại hoặc cái chết",
                    "9. Phần thưởng: đạt được mục tiêu hoặc kiến thức"
                ]
            },
            "phase_3": {
                "title": "PHÁN 3: Trở về hoàn thiện",
                "steps": [
                    "10. Con đường trở về: quyết định về nhà",
                    "11. Phục sinh: thử thách cuối cùng cùng kiến thức mới",
                    "12. Trở về với phép thưởng: mang lại giá trị cho cộng đồng"
                ]
            }
        }
        
        if theme:
            outline["theme_integration"] = f"Tích hợp chủ đề '{theme}' vào mỗi giai đoạn của hành trình"
        
        return outline
    
    def _generate_fable_outline(self, structure: Dict, genre: str, theme: str) -> Dict:
        """Generate outline for fable structure"""
        outline = {
            "introduction": {
                "title": "Giới thiệu (15%)",
                "elements": [
                    "Giới thiệu nhân vật và đặc tính chính",
                    "Thiết lập bối cảnh",
                    "Đề xuất thói quen hoặc phẩm chất sẽ được kiểm tra"
                ]
            },
            "development": {
                "title": "Phát triển (25%)",
                "elements": [
                    "Tạo tình huống thử thách",
                    "Lựa chọn quan trọng của nhân vật",
                    "Gặp nhân vật tương phản"
                ]
            },
            "conflict": {
                "title": "Xung đột (35%)",
                "elements": [
                    "Hậu quả của lựa chọn",
                    "Leo thang vấn đề",
                    "Điểm quyết định",
                    "Khủng hoảng cao điểm"
                ]
            },
            "resolution": {
                "title": "Giải quyết (25%)",
                "elements": [
                    "Kết quả cuối cùng",
                    "Học hỏi từ thất bại/thành công",
                    "Bài học đạo đức",
                    "Thông điệp cho độc giả"
                ]
            }
        }
        
        if theme:
            outline["moral_focus"] = f"Bài học cốt lõi về '{theme}' sẽ thể hiện qua hành động và kết quả"
        
        return outline
    
    def _generate_circular_outline(self, structure: Dict, genre: str, theme: str) -> Dict:
        """Generate circular structure outline"""
        outline = {
            "phases": [
                {
                    "phase": 1,
                    "title": "Thái độ ban đầu",
                    "description": "Giới thiệu thế giới và vấn đề hiện tại"
                },
                {
                    "phase": 2, 
                    "title": "Thử thách xuất hiện",
                    "description": "Sự kiện kích hoạt thay đổi"
                },
                {
                    "phase": 3,
                    "title": "Hành trình đổi thay",
                    "description": "Quá trình vượt qua thử thách và học hỏi"
                },
                {
                    "phase": 4,
                    "title": "Thấu hiểu sâu sắc",
                    "description": "Nhận ra sự thật về bản thân và thế giới"
                },
                {
                    "phase": 5,
                    "title": "Trở lại ban đầu",
                    "description": "Quay lại đầu điểm nhưng với tầm nhìn mới"
                }
            ]
        }
        
        return outline
    
    def format_structure(self, structure: Dict, format_type: str = "markdown") -> str:
        """Format structure for output"""
        if format_type == "markdown":
            return self._format_markdown(structure)
        elif format_type == "json":
            return json.dumps(structure, ensure_ascii=False, indent=2)
        elif format_type == "outline":
            return self._format_outline(structure)
        else:
            return str(structure)
    
    def _format_markdown(self, structure: Dict) -> str:
        """Format structure as markdown"""
        lines = []
        lines.append(f"# {structure['name']}")
        lines.append(f"*{structure['description']}*")
        lines.append("")
        
        if "genre" in structure:
            lines.append(f"**Thể loại:** {structure['genre']}")
            lines.append("")
        
        if "theme" in structure:
            lines.append(f"**Chủ đề:** {structure['theme']}")
            lines.append("")
        
        if "outline" in structure:
            outline = structure["outline"]
            
            for key, value in outline.items():
                if isinstance(value, dict) and "title" in value:
                    lines.append(f"## {value['title']}")
                    
                    if "steps" in value:
                        for step in value["steps"]:
                            lines.append(f"- {step}")
                    elif "elements" in value:
                        for element in value["elements"]:
                            lines.append(f"- {element}")
                    
                    lines.append("")
                
                elif key == "genre_notes":
                    lines.append("### Ghi chú thể loại")
                    for note in value:
                        lines.append(f"- {note}")
                    lines.append("")
                
                elif key == "theme_integration":
                    lines.append(f"### Tích hợp chủ đề")
                    lines.append(f"*{value}*")
                    lines.append("")
        
        if "genre_modifiers" in structure:
            lines.append("## Yếu tố thể loại đặc trưng")
            for modifier in structure["genre_modifiers"]:
                lines.append(f"- {modifier}")
            lines.append("")
        
        if "theme_elements" in structure:
            lines.append("## Yếu tố chủ đề")
            for element in structure["theme_elements"]:
                lines.append(f"- {element}")
        
        return "\n".join(lines)
    
    def _format_outline(self, structure: Dict) -> str:
        """Format structure as numbered outline"""
        lines = []
        lines.append(f"{structure['name']}")
        lines.append("=" * len(structure['name']))
        lines.append("")
        
        if "outline" in structure:
            outline = structure["outline"]
            
            for main_key, main_value in outline.items():
                if isinstance(main_value, dict) and "title" in main_value:
                    lines.append(f"{main_key.upper()}: {main_value['title']}")
                    
                    if "steps" in main_value:
                        for i, step in enumerate(main_value["steps"], 1):
                            lines.append(f"  {i}. {step}")
                    elif "elements" in main_value:
                        for i, element in enumerate(main_value["elements"], 1):
                            lines.append(f"  {i}. {element}")
                    
                    lines.append("")
        
        if "genre_modifiers" in structure:
            lines.append("YÊU TỐ THỂ LOẠI:")
            for modifier in structure["genre_modifiers"]:
                lines.append(f"  • {modifier}")
            lines.append("")
        
        return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Generate story structure")
    parser.add_argument("--model", required=True,
                       choices=["three_act", "hero_journey", "fable_structure", "circular"])
    parser.add_argument("--genre", 
                       choices=["fairytale", "fable", "children", "adventure"])
    parser.add_argument("--theme",
                       choices=["friendship", "honesty", "courage", "kindness", 
                               "perseverance", "wisdom", "love"])
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--format", default="markdown",
                       choices=["markdown", "json", "outline"])
    
    args = parser.parse_args()
    
    helper = StoryStructureHelper()
    
    try:
        structure = helper.generate_structure(
            model=args.model,
            genre=args.genre,
            theme=args.theme,
            format_type=args.format
        )
        
        formatted = helper.format_structure(structure, args.format)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(formatted)
            print(f"Structure saved to {args.output}")
        else:
            print(formatted)
            
    except Exception as e:
        print(f"Error generating structure: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
