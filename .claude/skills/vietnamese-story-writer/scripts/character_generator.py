#!/usr/bin/env python3
"""
Vietnamese Character Generator - Công cụ phát triển nhân vật truyện

Usage:
    python character_generator.py --role protagonist --type human --name Nguyen
    python character_generator.py --role antagonist --type animal --species dragon
    python character_generator.py --role supporting --type magical --name FairyDust
"""

import argparse
import json
import random
from typing import Dict, List, Any

class VietnameseCharacterGenerator:
    def __init__(self):
        self.human_names = self._load_human_names()
        self.animal_characters = self._load_animal_characters()
        self.magical_beings = self._load_magical_beings()
        self.personality_traits = self._load_personality_traits()
        self.appearances = self._load_appearance_descriptions()
        self.backgrounds = self._load_backgrounds()
    
    def _load_human_names(self) -> Dict[str, List[str]]:
        """Load Vietnamese human names"""
        return {
            "male": [
                "An", "Bảo", "Cường", "Dũng", "Hùng", "Lâm", "Minh", 
                "Quân", "Tùng", "Vinh", "Hoàng", "Long", "Nam", "Phúc",
                "Sơn", "Thái", "Thể", "Tiến", "Trung", "Tuấn"
            ],
            "female": [
                "An", "Chi", "Duyên", "Hà", "Lan", "Mai", "Nga", 
                "Quỳnh", "Thảo", "Trang", "Anh", "Giang", "Hoa", "Khánh",
                "Linh", "Ngọc", "Phương", "Thanh", "Thu", "Yến"
            ],
            "surnames": [
                "Nguyễn", "Trần", "Lê", "Phạm", "Huỳnh", "Hoàng", 
                "Phan", "Vũ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", 
                "Dương", "Lý", "Đinh"
            ]
        }
    
    def _load_animal_characters(self) -> Dict[str, Dict[str, Any]]:
        """Load animal character archetypes"""
        return {
            "ant": {
                "names": ["Con Kiến", "Bé Kiến", "Kiến Cần Cù", "Bé Kiến Thông Minh"],
                "traits": ["cần cù", "chăm chỉ", "có tổ chức", "đoàn kết", "nhỏ bé nhưng mạnh mẽ"],
                "appearance": "nhỏ bé, màu đen hoặc đỏ, luôn làm việc không mệt mỏi",
                "abilities": ["khiêng vật nặng", "làm việc nhóm", "tìm đường đi"]
            },
            "grasshopper": {
                "names": ["Con Dế", "Dế Mèn", "Chú Dế Vui Tính", "Dế Ca"],
                "traits": ["yêu âm nhạc", "vui vẻ", "chơi bời", "ít làm việc"],
                "appearance": "màu xanh, có cánh, lúc nào cũng nhảy múa",
                "abilities": ["nhảy cao", "kêu tiếng reo vui", "chơi nhạc cụ"]
            },
            "turtle": {
                "names": ["Con Rùa", "Cụ Rùa", "Rùa Chậm Rãi", "Ông Rùa"],
                "traits": ["kiên trì", "thông thái", "bền bỉ", "điềm tĩnh"],
                "appearance": "mang mai to, di chuyển chậm rãi, đôi mắt già dặn",
                "abilities": ["sống lâu", "bơi giỏi", "chịu đựng tốt"]
            },
            "rabbit": {
                "names": ["Con Thỏ", "Bé Thỏ", "Thỏ Nhanh Nhẹn", "Thỏ Trắng"],
                "traits": ["nhanh nhẹn", "thông minh", "hiếu kỳ", "tinh nghịch"],
                "appearance": "lông trắng mịn, tai dài, mắt sáng ngời",
                "abilities": ["chạy nhanh", "nhảy cao", "nhạy bén"]
            },
            "fox": {
                "names": ["Con Cáo", "Chú Cáo", "Cáo Hùng Hổ", "Anh Cáo"];
                "traits": ["xảo quyệt", "thông minh", "lợi dụng", "hiểu biết"],
                "appearance": "lông vàng đỏ, đuôi bus, mắt tinh ranh",
                "abilities": ["lừa gạt", "tìm đường lắt léo", "trốn kẻ thù"]
            },
            "lion": {
                "names": ["Sư Tử", "Ông Vua Sư Tử", "Sư Tử Oai Hùng"],
                "traits": ["dũng cảm", "mạnh mẽ", "oai phong", "công bằng"],
                "appearance": "bờm vàng dày, thân hình to lớn, tiếng gầm vang dội",
                "abilities": ["dẫn đầu", "bảo vệ đàn", "sức mạnh phi thường"]
            },
            "elephant": {
                "names": ["Con Voi", "Chú Voi", "Ông Voi Đầu Đội", "Voi Thông Thái"],
                "traits": ["thông thái", "hiền lành", "mạnh mẽ", "trí nhớ tốt"],
                "appearance": "xám lớn, vòi dài, tai rộng, ngà trắng",
                "abilities": ["nhớ tốt", "khiêng vật nặng", "lội nước sâu"]
            },
            "bird": {
                "names": ["Con Chim", "Bé Chim", "Chiền Chiện", "Chim Thánh"],
                "traits": ["tự do", "hi vọng", "thông minh", "năng động"],
                "appearance": "lông màu sắc sặc sỡ, cánh rộng, tiếng hót trong trẻo",
                "abilities": ["bay cao", "thấy từ xa", "thông điệp nhanh chóng"]
            }
        }
    
    def _load_magical_beings(self) -> Dict[str, Dict[str, Any]]:
        """Load magical character archetypes"""
        return {
            "fairy": {
                "names": ["Công Chúa", "Tiên Nữ", "Chú Tiên", "Bé Tiên"],
                "traits": ["bí ẩn", "tốt bụng", "khéo léo", "thuần khiết"],
                "appearance": "màu sắc sặc sỡ, đôi cánh trong suốt, ánh sáng huyền ảo",
                "powers": ["phép thuật", "biến hình", "chữa bệnh", "bay lượn"]
            },
            "dragon": {
                "names": ["Rồng Thiêng", "Quái Vật", "Rồng Lửa", "Thần Long"],
                "traits": ["mạnh mẽ", "oai nghiêm", "bảo vệ", "cổ xưa"],
                "appearance": "vảy kim loại, mắt đỏ rực, hơi lửa, hình dạng hùng vĩ",
                "powers": ["phở lửa", "bay lượn", "sức mạnh siêu nhiên", "bảo vệ kho báu"]
            },
            "wizard": {
                "names": ["Phù Thủy", "Thần Bà", "Đạo Sĩ", "Pháp Sư"],
                "traits": ["thông thái", "bí ẩn", "quyền lực", "hiếu học"],
                "appearance": "áo choàng dài, gậy phép thuật, râu dài, mắt sắc sảo",
                "powers": ["chiêu hồn", "đọc vị tương lai", "thuốc độc", "phép thuật cổ xưa"]
            },
            "unicorn": {
                "names": ["Kỳ Lân", "Ngựa Đơn Horn", "Thú Thánh", "Biểu Tượng Tinh Khiết"],
                "traits": ["trong trắng", "tinh khiết", "chữa lành", "hòa bình"],
                "appearance": "lông trắng muốt, sừng xoắn kỳ diệu, ánh sáng bao quanh",
                "powers": ["chữa lành mọi vết thương", "xác định sự thật", "thanh tắc", "bảo vệ khỏi cái ác"]
            }
        }
    
    def _load_personality_traits(self) -> Dict[str, List[str]]:
        """Load personality traits by category"""
        return {
            "positive": [
                "dũng cảm", "thông minh", "tử tế", "cần cù", "honest", 
                "loyal", "generous", "patient", "determined", "optimistic",
                "creative", "curious", "compassionate", "wise", "humble"
            ],
            "negative": [
                "lười biếng", "ghê tởm", "gian hùng", "tớrớn", "ghen tị",
                "hung hăng", "vô trách nhiệm", "tốt bụng", "dễ dàng bị tác động", "vô kỷ luật"
            ],
            "neutral": [
                "thận trọng", "đơn độc", "phức tạp", "bí ẩn", "tradition",
                "calm", "logic", "intuitive", "adventurous", "sensitive"
            ]
        }
    
    def _load_appearance_descriptions(self) -> Dict[str, List[str]]:
        """Load physical appearance descriptions"""
        return {
            "hair": ["đen nhánh", "nâu", "vàng", "trắng", "bạc", "xoăn", "thẳng", "dai"],
            "eyes": ["đen huyền", "nâu ấm", "xanh lá", "xanh dương", "sáng ngời", "sâu thẳm", "thông minh"],
            "build": ["nhỏ nhắn", "trung bình", "to lớn", "mạnh mẽ", "thon gọn", "vạm vỡ"],
            "clothing": ["trang phục đơn giản", "áo dài", "quần áo màu sắc", "áo choàng", "trang phục hoàng gia"],
            "distinguishing": ["vết sẹo nhỏ", "xăm hình kỳ lạ", "trang sức quý giá", "vũ khí đặc biệt"]
        }
    
    def _load_backgrounds(self) -> List[str]:
        """Load character backgrounds"""
        return [
            "đến từ một ngôi làng nhỏ ở miền quê",
            "mất cha mẹ từ nhỏ và sống một mình",
            "con của một người thợ thủ công tài ba",
            "được đào tạo từ một pháp sư thông thái",
            "kế thừa di sản từ tổ tiên",
            "là người ngoài cuộc trong cộng đồng",
            "đã từng trải qua một bi kịch lớn",
            "câu chuyện bí ẩn che giấu bản danh thực sự"
        ]
    
    def generate_character(self, role: str, character_type: str = "human", 
                          name: str = None, species: str = None, **kwargs) -> Dict[str, Any]:
        """Generate character based on parameters"""
        
        character = {
            "role": role,
            "type": character_type,
            "name": name,
            "species": species,
            "generated_at": "2025-11-20"
        }
        
        # Generate name if not provided
        if not name:
            if character_type == "human":
                surname = random.choice(self.human_names["surnames"])
                given_name = random.choice(self.human_names["male"] if random.random() > 0.5 
                                         else self.human_names["female"])
                character["full_name"] = f"{surname} {given_name}"
                character["name"] = given_name
            elif character_type == "animal":
                animal_data = self.animal_characters.get(species or random.choice(list(self.animal_characters.keys())))
                character["name"] = random.choice(animal_data["names"])
            elif character_type == "magical":
                magic_data = self.magical_beings.get(species or random.choice(list(self.magical_beings.keys())))
                character["name"] = random.choice(magic_data["names"])
        
        # Generate personality based on role
        if role == "protagonist" or role == "hero":
            traits = random.sample(self.personality_traits["positive"], 3)
            traits.append(random.choice(self.personality_traits["neutral"]))
        elif role == "antagonist" or role == "villain":
            traits = random.sample(self.personality_traits["negative"], 2)
            traits.append(random.choice(self.personality_traits["positive"]))
        else:  # supporting
            traits = random.sample(self.personality_traits["neutral"], 2)
            traits.append(random.choice(self.personality_traits["positive"]))
        
        character["personality_traits"] = traits
        character["main_trait"] = traits[0]  # Primary trait
        
        # Generate appearance and abilities based on type
        if character_type == "human":
            character.update(self._generate_human_appearance())
            character["background"] = random.choice(self.backgrounds)
        elif character_type == "animal":
            animal_data = self.animal_characters.get(species or "ant", self.animal_characters["ant"])
            character.update({
                "appearance": animal_data["appearance"],
                "abilities": animal_data["abilities"],
                "natural_traits": animal_data["traits"]
            })
        elif character_type == "magical":
            magic_data = self.magical_beings.get(species or "fairy", self.magical_beings["fairy"])
            character.update({
                "appearance": magic_data["appearance"],
                "powers": magic_data["powers"],
                "magical_traits": magic_data["traits"]
            })
        
        # Generate age and status
        if character_type == "human":
            age_ranges = {
                "child": (6, 12),
                "teen": (13, 18), 
                "young_adult": (19, 30),
                "adult": (31, 50),
                "elder": (51, 80)
            }
            # Choose appropriate age range based on story type
            age_category = random.choice(list(age_ranges.keys()))
            min_age, max_age = age_ranges[age_category]
            character["age"] = random.randint(min_age, max_age)
            character["age_category"] = age_category
        elif character_type == "animal":
            categories = ["young", "adult", "wise_old"]
            character["age_category"] = random.choice(categories)
        elif character_type == "magical":
            categories = ["young_magic", "ancient", "timeless"]
            character["age_category"] = random.choice(categories)
        
        return character
    
    def _generate_human_appearance(self) -> Dict[str, str]:
        """Generate random human appearance"""
        return {
            "hair": random.choice(self.appearance_descriptions["hair"]),
            "eyes": random.choice(self.appearance_descriptions["eyes"]),
            "build": random.choice(self.appearance_descriptions["build"]),
            "clothing": random.choice(self.appearance_descriptions["clothing"]),
            "distinguishing_feature": random.choice(self.appearance_descriptions["distinguishing"])
        }
    
    def format_character_description(self, character: Dict[str, Any]) -> str:
        """Format character as readable description"""
        description = [f"**{character['name'].title()}**"]
        
        if "full_name" in character:
            description.append(f"Họ và tên: {character['full_name']}")
        
        description.append(f"Vai trò: {character['role']}")
        description.append(f"Loại: {character['type']}")
        
        if "age" in character:
            description.append(f"Tuổi: {character['age']}")
        
        description.append(f"Tính cách chính: {', '.join(character['personality_traits'])}")
        
        if "appearance" in character:
            description.append(f"Ngoại hình: {character['appearance']}")
        
        if "hair" in character:
            description.append(f"Tóc: {character['hair']}")
            description.append(f"Mắt: {character['eyes']}")
            description.append(f"Dáng người: {character['build']}")
            description.append(f"Trang phục: {character['clothing']}")
        
        if "abilities" in character:
            description.append(f"Khả năng đặc biệt: {', '.join(character['abilities'])}")
        
        if "powers" in character:
            description.append(f"Sức mạnh phép thuật: {', '.join(character['powers'])}")
        
        if "background" in character:
            description.append(f"Nền tảng: {character['background']}")
        
        return "\n".join(description)
    
    def export_character(self, character: Dict[str, Any], output_path: str = None) -> str:
        """Export character to file or return as string"""
        formatted = self.format_character_description(character)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted)
                f.write("\n\n---\n\n")
                json.dump(character, f, ensure_ascii=False, indent=2)
            return f"Character saved to {output_path}"
        
        return formatted

def main():
    parser = argparse.ArgumentParser(description="Generate Vietnamese story characters")
    parser.add_argument("--role", required=True,
                       choices=["protagonist", "antagonist", "supporting", "hero", "villain", "sidekick"])
    parser.add_argument("--type", default="human",
                       choices=["human", "animal", "magical"])
    parser.add_argument("--name", help="Character name")
    parser.add_argument("--species", help="Species for animal/magical characters")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--format", default="description",
                       choices=["description", "json", "both"])
    
    args = parser.parse_args()
    
    generator = VietnameseCharacterGenerator()
    
    try:
        character = generator.generate_character(
            role=args.role,
            character_type=args.type,
            name=args.name,
            species=args.species
        )
        
        if args.format == "json":
            output = json.dumps(character, ensure_ascii=False, indent=2)
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(output)
                print(f"Character JSON saved to {args.output}")
            else:
                print(output)
        
        elif args.format == "description":
            description = generator.format_character_description(character)
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(description)
                print(f"Character description saved to {args.output}")
            else:
                print(description)
        
        else:  # both
            result = generator.export_character(character, args.output)
            print(result)
            
    except Exception as e:
        print(f"Error generating character: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
