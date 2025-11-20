#!/usr/bin/env python3
"""
Vietnamese Story Generator - Công cụ tạo truyện tiếng Việt

Usage:
    python story_generator.py --genre fairytale --theme friendship --output story.md
    python story_generator.py --genre fable --theme honesty --format illustrated
    python story_generator.py --genre children --theme adventure --length medium
"""

import argparse
import json
import random
from datetime import datetime
from pathlib import Path

class VietnameseStoryGenerator:
    def __init__(self):
        self.story_templates = self._load_story_templates()
        self.character_names = self._load_character_names()
        self.locations = self._load_locations()
        
    def _load_story_templates(self):
        """Load story structure templates for different genres"""
        return {
            "fairytale": {
                "opening": [
                    "Ngày xửa ngày xưa, trong một khu rừng rậm rạp có một {main_character} rất {adjective}.",
                    "Từ thuở khai thiên lập địa, ở một ngôi {location} gần làng có một câu chuyện về {main_character}.",
                    "Trong một đất nước xa xôi, có một {main_character} nổi tiếng vì {special_trait}."
                ],
                "conflict": [
                    "Một ngày nọ, {antagonist} đến và gây ra {problem}.",
                    "Bỗng nhiên, {problem} xảy ra khiến cả làng phải lo lắng.",
                    "{main_character} phải đối mặt với thử thách {challenge}."
                ],
                "resolution": [
                    "Nhờ {positive_trait}, {main_character} đã giải quyết được vấn đề.",
                    "Cuối cùng, {solution} đã giúp mọi thứ trở lại bình thường.",
                    "Sự {moral} đã chiến thắng {negative_force}."
                ],
                "ending": [
                    "Và từ đó về sau, {main_character} sống hạnh phúc mãi mãi.",
                    "Câu chuyện về {main_character} được kể lại từ thế hệ này sang thế hệ khác.",
                    "Mọi người học được bài học sâu sắc về {lesson}."
                ]
            },
            "fable": {
                "opening": [
                    "Trong một khu rừng nọ, có một {animal1} đang {action1}.",
                    "Từ xưa, trong một {location} có hai người bạn là {animal1} và {animal2}.",
                    "Ngày ngày, {animal1} luôn {habit}."
                ],
                "conflict": [
                    "Đến một ngày, {animal2} đến và {conflict_action}.",
                    "Mùa đông đến, {problem} xảy ra với {animal1}.",
                    "{situation} khiến {animal1} phải đối mặt với sự thật."
                ],
                "resolution": [
                    "Sau khi trải qua {experience}, {animal1} nhận ra {realization}.",
                    "Cuối cùng, {consequence} xảy ra với {animal2}.",
                    "{moral} đã được chứng minh đúng."
                ],
                "ending": [
                    "Bài học rút ra là: {moral_lesson}.",
                    "Vậy nên câu chuyện dạy chúng ta rằng {lesson}."
                ]
            },
            "children": {
                "opening": [
                    "Có bạn tên là {child_name}, {age} tuổi, rất thích {hobby}.",
                    "Một buổi sáng đẹp trời, {child_name} quyết định đi {activity}.",
                    "{child_name} là một đứa trẻ {adjective} sống ở {place_type}."
                ],
                "conflict": [
                    "Bất ngờ, {challenge} xuất hiện trước mắt {child_name}.",
                    "Khi đang {activity}, {child_name} phát hiện ra {discovery}.",
                    "Một việc gì đó kỳ lạ đã xảy ra: {strange_event}."
                ],
                "resolution": [
                    "Sau nhiều nỗ lực, {child_name} đã {achievement}.",
                    "Với sự giúp đỡ của {helper}, {child_name} giải quyết được vấn đề.",
                    "Bằng trí thông minh và lòng dũng cảm, {child_name} đã {success}."
                ],
                "ending": [
                    "{child_name} học được rằng {value_lesson}.",
                    "Từ hôm đó, {child_name} đã trở nên {improvement}."
                ]
            },
            "adventure": {
                "opening": [
                    "{hero_name} nhận được một sứ mệnh {mission_type}.",
                    "Trong một thế giới {world_type}, có một cuộc {quest_name}.",
                    "{hero_name} sống ở {hometown} đã có một cuộc đời bình thường cho đến khi {event}."
                ],
                "conflict": [
                    "{villain_name} đang âm mưu {evil_plan}.",
                    "{danger} đe dọa đến thế giới {world_name}.",
                    "Cuộc hành trình của {hero_name} gặp phải {obstacle}."
                ],
                "resolution": [
                    "{hero_name} phải tập hợp {allies} để đối mặt với {villain_name}.",
                    "Sau nhiều thử thách, {hero_name} tìm được {artifact} để {purpose}.",
                    "Cuộc chiến quyết định xảy ra tại {battle_location}."
                ],
                "ending": [
                    "Thế giới được cứu, và {hero_name} trở thành {title}.",
                    "Bình yên trở lại với các bài học sâu sắc về {theme}."
                ]
            }
        }
    
    def _load_character_names(self):
        """Load Vietnamese character names by category"""
        return {
            "human_male": ["An", "Bảo", "Cường", "Dũng", "Hùng", "Lâm", "Minh", "Quân", "Tùng", "Vinh"],
            "human_female": ["An", "Chi", "Duyên", "Hà", "Lan", "Mai", "Nga", "Quỳnh", "Thảo", "Trang"],
            "animals": {
                "ant": ["con kiến", "bé Kiến", "chú Kiến Cần Cù"],
                "grasshopper": ["con dế", "chú Dế Mèn", "bé Dế"],
                "turtle": ["con rùa", "cụ Rùa", "chú Rùa Chậm Rãi"],
                "rabbit": ["con thỏ", "bé Thỏ", "chú Thỏ Nhanh Nhẹn"],
                "fox": ["con cáo", "chú Cáo Hùng Hổ", "bé Cáo"],
                "lion": ["con sư tử", "vua Sư Tử"],
                "elephant": ["con voi", "chú Vojià", "ông Voi Đầu Đội"],
                "bird": ["con chim", "bé Chim Thánh", "chú Chiền Chiện"]
            }
        }
    
    def _load_locations(self):
        """Load story locations"""
        return {
            "village": ["làng quê", "xóm nhỏ", "ngôi làng bình yên"],
            "forest": ["khu rừng rậm rạp", "rừng xanh", "rừng cổ tích"],
            "castle": ["ngôi lầu", "đền đài", "lâu đài cổ"],
            "river": ["dòng sông", "bờ sông", "cầu sông"],
            "mountain": ["ngọn núi", "đỉnh cao", "dãy núi hùng vĩ"],
            "garden": ["khu vườn", "vườn cây", "khu sân sau"]
        }
    
    def generate_character(self, role_type, character_type=None):
        """Generate character based on type and role"""
        if character_type == "human":
            names = self.character_names["human_male"] if random.random() > 0.5 else self.character_names["human_female"]
            return random.choice(names)
        elif character_type == "animal":
            animal_type = random.choice(list(self.character_names["animals"].keys()))
            return random.choice(self.character_names["animals"][animal_type])
        else:
            return random.choice(["người bạn", "sinh vật kỳ lạ", "nhân vật bí ẩn"])
    
    def generate_story(self, genre, theme, length="medium", format_type="markdown"):
        """Generate story based on genre and theme"""
        if genre not in self.story_templates:
            raise ValueError(f"Genre '{genre}' not supported. Available: {list(self.story_templates.keys())}")
        
        template = self.story_templates[genre]
        
        # Generate content based on template
        story_elements = {
            "main_character": self.generate_character("protagonist", "human" if genre not in ["fable"] else "animal"),
            "adjective": random.choice(["tốt bụng", "dũng cảm", "thông minh", "cần cù", "nhân hậu"]),
            "location": random.choice(list(self.locations.values())[0]),
            "antagonist": self.generate_character("antagonist", "animal" if genre == "fable" else "human"),
            "problem": self._generate_problem(theme),
            "moral": self._generate_moral(theme),
            "positive_trait": random.choice(["lòng tốt", "trí tuệ", "sự kiên trì", "lòng dũng cảm"]),
            "lesson": self._extract_lesson(theme)
        }
        
        # Build story
        story_parts = []
        
        # Opening
        opening = random.choice(template["opening"]).format(**story_elements)
        story_parts.append(f"# {self._generate_title(genre, theme)}\n\n{opening}")
        
        # Middle sections
        if genre == "fairytale":
            conflict = random.choice(template["conflict"]).format(**story_elements)
            resolution = random.choice(template["resolution"]).format(**story_elements)
            story_parts.extend([f"\n\n{conflict}", f"\n\n{resolution}"])
        
        elif genre == "fable":
            conflict = random.choice(template["conflict"]).format(**story_elements)
            resolution = random.choice(template["resolution"]).format(**story_elements)
            moral_lesson = self._generate_fable_moral(theme)
            ending = template["ending"][0].format(moral_lesson=moral_lesson)
            story_parts.extend([f"\n\n{conflict}", f"\n\n{resolution}", f"\n\n{ending}"])
        
        elif genre == "children":
            child_name = random.choice(self.character_names["human_male"] + self.character_names["human_female"])
            story_elements["child_name"] = child_name
            story_elements["age"] = random.randint(7, 12)
            story_elements["hobby"] = random.choice(["đọc sách", "khám phá", "vẽ tranh", "chơi thể thao"])
            
            conflict = random.choice(template["conflict"]).format(**story_elements)
            resolution = random.choice(template["resolution"]).format(**story_elements)
            lesson = random.choice(template["ending"]).format(**story_elements)
            story_parts.extend([f"\n\n{conflict}", f"\n\n{resolution}", f"\n\n{lesson}"])
        
        elif genre == "adventure":
            hero_name = random.choice(self.character_names["human_male"])
            story_elements["hero_name"] = hero_name
            story_elements["mission_type"] = random.choice(["cứu vớt", "khám phá", "tìm kho báu", "đánh bại quái vật"])
            
            conflict = random.choice(template["conflict"]).format(**story_elements)
            resolution = random.choice(template["resolution"]).format(**story_elements)
            ending = template["ending"][0].format(**story_elements)
            story_parts.extend([f"\n\n{conflict}", f"\n\n{resolution}", f"\n\n{ending}"])
        
        story = "".join(story_parts)
        
        # Add format-specific additions
        if format_type == "illustrated":
            story += "\n\n---\n\n**Gợi ý minh họa:**\n"
            story += f"- Cảnh opening: {story_elements['location']}\n"
            story += f"- Nhân vật chính: {story_elements['main_character']}\n"
            story += "- Thêm màu sắc tươi sáng và hình ảnh thân thiện\n"
        
        return story
    
    def _generate_problem(self, theme):
        """Generate problem based on theme"""
        problems = {
            "friendship": "mất đi người bạn thân",
            "honesty": "lời nói dối bị phát hiện",
            "courage": "phải đối mặt với nỗi sợ hãi",
            "kindness": "ai đó đối xử tệ bạc",
            "perseverance": "thất bại nhiều lần",
            "wisdom": "quyết định sai lầm",
            "love": "nỗi cô đơn và bị bỏ lại"
        }
        return problems.get(theme, "vấn đề khó khăn bất ngờ")
    
    def _generate_moral(self, theme):
        """Generate moral based on theme"""
        morals = {
            "friendship": "tình bạn thật sự quý giá",
            "honesty": "sự trung thực luôn được trọng",
            "courage": "dũng cảm đối mặt thử thách",
            "kindness": "lòng tốt bụng sẽ được đền đáp",
            "perseverance": "kiên trì cuối cùng sẽ thành công",
            "wisdom": "trí tuệ giúp ta đưa ra lựa chọn đúng",
            "love": "tình yêu thương chữa lành mọi vết thương"
        }
        return morals.get(theme, "lòng tốt luôn chiến thắng")
    
    def _extract_lesson(self, theme):
        """Extract lesson from theme"""
        lessons = {
            "friendship": "giữ gìn tình bạn",
            "honesty": "luôn nói thật",
            "courage": "dũng cảm đối mặt khó khăn",
            "kindness": "treat others with kindness",
            "perseverance": "không bao giờ bỏ cuộc",
            "wisdom": "học hỏi và suy nghĩ cẩn thận",
            "love": "yêu thương và chia sẻ"
        }
        return lessons.get(theme, "hãy là người tốt")
    
    def _generate_title(self, genre, theme):
        """Generate appropriate title"""
        titles = {
            "fairytale": [
                "Câu Chuyện Về Lòng Trung Thực", 
                "Chuyện Cổ Tích Về Tình Bạn",
                "Truyện Cổ Tích Về Lòng Dũng Cảm"
            ],
            "fable": [
                "Kiến và Dế",
                "Chú Rùa và Chú Thỏ", 
                "Cáo và Nho Đăng"
            ],
            "children": [
                "Cuộc Phiêu Lưu Của Bé An",
                "Bạn Thật Tuyệt Vời",
                "Hành Trình Kỳ Diệu"
            ],
            "adventure": [
                "Người Dũng Sĩ Bất Đắc Dĩ",
                "Cuộc Săn Kho Báu",
                "Hành Trình Đến Thế Giới Mới"
            ]
        }
        genre_titles = titles.get(genre, ["Một Câu Chuyện Hay"])
        return random.choice(genre_titles)
    
    def _generate_fable_moral(self, theme):
        """Generate specific moral for fables"""
        morals = {
            "friendship": "Giúp bạn lúc khó khăn là giúp chính mình.",
            "honesty": "Gieo nào gặt nấy - sự thật luôn chiến thắng.", 
            "diligence": "Cần cù bù thông minh, lười biếng gặt lấy thất bại.",
            "perserverance": "Kiên trì cuối cùng sẽ đến đích.",
            "wisdom": "Trí tuệ quý hơn sức mạnh."
        }
        return morals.get(theme, "Hãy sống thật với chính mình.")

def main():
    parser = argparse.ArgumentParser(description="Generate Vietnamese stories")
    parser.add_argument("--genre", required=True, 
                       choices=["fairytale", "fable", "children", "adventure"])
    parser.add_argument("--theme", required=True,
                       choices=["friendship", "honesty", "courage", "kindness", 
                               "perseverance", "wisdom", "love"])
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--format", default="markdown", 
                       choices=["markdown", "plain", "illustrated"])
    parser.add_argument("--length", default="medium", 
                       choices=["short", "medium", "long"])
    
    args = parser.parse_args()
    
    generator = VietnameseStoryGenerator()
    
    try:
        story = generator.generate_story(args.genre, args.theme, args.length, args.format)
        
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(story, encoding='utf-8')
            print(f"Story saved to {args.output}")
        else:
            print(story)
            
    except Exception as e:
        print(f"Error generating story: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
