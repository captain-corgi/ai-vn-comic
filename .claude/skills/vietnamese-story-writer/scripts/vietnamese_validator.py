#!/usr/bin/env python3
"""
Vietnamese Language Validator - Công cụ kiểm tra và cải thiện chất lượng tiếng Việt

Usage:
    python vietnamese_validator.py --input story.md --check grammar,vocabulary
    python vietnamese_validator.py --input story.md --suggestions --output improved.md
    python vietnamese_validator.py --text "sample text" --quick-check
"""

import argparse
import re
import json
from typing import Dict, List, Set, Tuple
from pathlib import Path

class VietnameseValidator:
    def __init__(self):
        self.common_grammar_errors = self._load_grammar_patterns()
        self.vocabulary_age_levels = self._load_age_vocabulary()
        self.style_guides = self._load_style_guidelines()
        self.inappropriate_terms = self._load_inappropriate_terms()
        
    def _load_grammar_patterns(self) -> Dict[str, List[Dict]]:
        """Load common Vietnamese grammar error patterns"""
        return {
            "subject_verb_agreement": [
                {"pattern": r"tôi[ ]+có[ ]+đi", "suggestion": "tôi đi", "message": "Không cần 'có' khi nói về hành động."},
                {"pattern": r"các?[ ]+họ[ ]+là[ ]+người", "suggestion": "họ là người", "message": "Ngữ pháp không chính xác."},
                {"pattern": r"thấy[ ]+rằng[ ]+rằng", "suggestion": "thấy rằng", "message": "Lặp từ 'rằng' không cần thiết."}
            ],
            " redundancies": [
                {"pattern": r"cùng[ ]+nhau", "suggestion": "cùng nhau", "message": "Viết đúng là 'cùng nhau'."},
                {"pattern": r"quan[ ]+trọng[ ]+lắm", "suggestion": "rất quan trọng", "message": "Dùng 'rất quan trọng' thay 'quan trọng lắm'."}
            ],
            "tense_errors": [
                {"pattern": r"đã[ ]+sẽ[ ]+\w+", "suggestion": "thay đổi thời gian", "message": "Không dùng cả 'đã' và 'sẽ' cùng lúc."},
                {"pattern": r"đang[ ]+đã[ ]+\w+", "suggestion": "thay đổi thời gian", "message": "Không dùng cả 'đang' và 'đã' cùng lúc."}
            ],
            "word_order": [
                {"pattern": r"rất[ ]+\w+[ ]+nhiều", "suggestion": "nhiều hơn", "message": "Thứ tự từ không chính xác."},
                {"pattern": r"thường[ ]+xuyên[ ]+\w+", "suggestion": "thường xuyên", "message": "Viết đúng là 'thường xuyên'."}
            ]
        }
    
    def _load_age_vocabulary(self) -> Dict[str, Dict[str, List[str]]]:
        """Load vocabulary appropriate for different age groups"""
        return {
            "preschool": {
                "appropriate": [
                    "mẹ", "bố", "bé", "chơi", "đi", "ăn", "ngủ", "cười", "đồ chơi",
                    "bạn", "sách", "hoa", "cây", "nhà", "trường", "con chó", "con mèo"
                ],
                "inappropriate": [
                    "phức tạp", "khó hiểu", "trừu tượng", "triết học", "chính trị"
                ]
            },
            "elementary": {
                "appropriate": [
                    "trường học", "bạn bè", "học tập", "đọc sách", "chơi thể thao",
                    "gia đình", "giúp đỡ", "chia sẻ", "lòng tốt", "dũng cảm"
                ],
                "inappropriate": [
                    "kinh tế", "xã hội", "pháp luật", "kỹ thuật phức tạp"
                ]
            },
            "middle_grade": {
                "appropriate": [
                    "phiêu lưu", "bí ẩn", "trình bày", "giải quyết", "thử thách",
                    "trách nhiệm", "honesty", "friendship", "courage"
                ],
                "inappropriate": [
                    "chính trị nặng", "kinh tế phức tạp", "khái niệm trừu tượng cao"
                ]
            },
            "young_adult": {
                "appropriate": [
                    "mối quan hệ", "trách nhiệm", "quyết định", "thành công", "thất bại",
                    "sự nghiệp", "tương lai", "giá trị", "nguyên tắc"
                ],
                "inappropriate": [
                    "ngôn ngữ cực kỳ phức tạp", "chủ đề không phù hợp lứa tuổi"
                ]
            }
        }
    
    def _load_style_guidelines(self) -> Dict[str, List[str]]:
        """Load Vietnamese writing style guidelines"""
        return {
            "children_stories": [
                "Dùng câu ngắn, dễ hiểu",
                "Tránh câu quá dài và phức tạp",
                "Sử dụng từ positive, vui vẻ",
                "Nhân từ với cảm xúc trẻ em",
                "Trừu tượng hóa khái niệm khó"
            ],
            "fairytales": [
                "Bắt đầu với cổ tích mở đầu: 'Ngày xửa ngày xưa'",
                "Nhân vật rõ ràng: tốt hoặc xấu",
                "Sử dụng tính từ so sánh đơn giản",
                "Lặp lại cấu trúc câu để dễ nhớ",
                "Kết thúc với bài học đạo đức"
            ],
            "modern_stories": [
                "Đa dạng cấu trúc câu",
                "Thể hiện sự phát triển nhân vật",
                "Tạo đối thoại tự nhiên",
                "Sử dụng văn phong phù hợp độ tuổi"
            ]
        }
    
    def _load_inappropriate_terms(self) -> Set[str]:
        """Load terms inappropriate for children's content"""
        return {
            # Add actual inappropriate Vietnamese terms here
            # This is a placeholder - implement based on your content guidelines
            "bạo lực", "đáng sợ", "khó chịu", "phàn nàn", "ghét"
        }
    
    def validate_text(self, text: str, checks: List[str] = None, 
                     target_age: str = "elementary") -> Dict[str, Any]:
        """Validate Vietnamese text comprehensively"""
        if checks is None:
            checks = ["grammar", "vocabulary", "style", "appropriateness"]
        
        results = {
            "text_length": len(text),
            "word_count": len(self._count_words(text)),
            "sentence_count": len(self._count_sentences(text)),
            "checks_performed": checks,
            "target_age": target_age,
            "issues": [],
            "suggestions": [],
            "overall_score": 0
        }
        
        # Grammar check
        if "grammar" in checks:
            grammar_issues = self._check_grammar(text)
            results["issues"].extend(grammar_issues)
        
        # Vocabulary check
        if "vocabulary" in checks:
            vocab_issues = self._check_vocabulary(text, target_age)
            results["issues"].extend(vocab_issues)
        
        # Style check
        if "style" in checks:
            style_issues = self._check_style(text, target_age)
            results["issues"].extend(style_issues)
        
        # Appropriateness check
        if "appropriateness" in checks:
            appropriate_results = self._check_appropriateness(text)
            results["issues"].extend(appropriate_results)
        
        # Calculate overall score
        results["overall_score"] = self._calculate_score(results)
        
        # Generate suggestions
        results["suggestions"] = self._generate_suggestions(results["issues"])
        
        return results
    
    def _count_words(self, text: str) -> List[str]:
        """Count Vietnamese words (handling multi-word compounds)"""
        # Simple word counting for Vietnamese
        words = re.findall(r'\b\w+\b', text, re.UNICODE)
        return words
    
    def _count_sentences(self, text: str) -> List[str]:
        """Count Vietnamese sentences"""
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _check_grammar(self, text: str) -> List[Dict]:
        """Check for common grammar errors"""
        issues = []
        
        for error_type, patterns in self.common_grammar_errors.items():
            for pattern_data in patterns:
                matches = re.finditer(pattern_data["pattern"], text, re.IGNORECASE)
                for match in matches:
                    issues.append({
                        "type": "grammar",
                        "error_type": error_type,
                        "position": match.start(),
                        "text_found": match.group(),
                        "suggestion": pattern_data["suggestion"],
                        "message": pattern_data["message"],
                        "severity": "medium"
                    })
        
        return issues
    
    def _check_vocabulary(self, text: str, target_age: str) -> List[Dict]:
        """Check vocabulary appropriateness for target age"""
        issues = []
        words = self._count_words(text)
        
        if target_age in self.vocabulary_age_levels:
            age_vocab = self.vocabulary_age_levels[target_age]
            
            # Check for inappropriate vocabulary
            for word in words:
                if word.lower() in age_vocab["inappropriate"]:
                    issues.append({
                        "type": "vocabulary",
                        "word": word,
                        "issue": "inappropriate_for_age",
                        "message": f"'{word}' không phù hợp với độ tuổi {target_age}",
                        "suggestion": "thay bằng từ đơn giản hơn",
                        "severity": "high"
                    })
        
        return issues
    
    def _check_style(self, text: str, target_age: str) -> List[Dict]:
        """Check writing style appropriateness"""
        issues = []
        sentences = self._count_sentences(text)
        
        # Check sentence length
        for i, sentence in enumerate(sentences):
            word_count = len(self._count_words(sentence))
            if word_count > 20:  # sentences too long for children
                issues.append({
                    "type": "style",
                    "issue": "sentence_too_long",
                    "sentence_index": i,
                    "word_count": word_count,
                    "message": f"Câu {i+1} quá dài ({word_count} từ). Cần chia nhỏ câu.",
                    "suggestion": "Chia thành 2-3 câu ngắn hơn",
                    "severity": "medium"
                })
        
        # Add other style checks based on target age
        return issues
    
    def _check_appropriateness(self, text: str) -> List[Dict]:
        """Check for inappropriate content"""
        issues = []
        words = self._count_words(text)
        
        for word in words:
            if word.lower() in self.inappropriate_terms:
                issues.append({
                    "type": "appropriateness",
                    "word": word,
                    "issue": "inappropriate_content",
                    "message": f"'{word}' không phù hợp với nội dung thiếu nhi",
                    "suggestion": "thay bằng từ tích cực hơn",
                    "severity": "high"
                })
        
        return issues
    
    def _calculate_score(self, results: Dict) -> int:
        """Calculate overall quality score (0-100)"""
        total_issues = len(results["issues"])
        base_score = 100
        
        # Deduct points based on issues
        score_deductions = 0
        for issue in results["issues"]:
            if issue["severity"] == "high":
                score_deductions += 10
            elif issue["severity"] == "medium":
                score_deductions += 5
            else:
                score_deductions += 2
        
        final_score = max(0, base_score - score_deductions)
        return final_score
    
    def _generate_suggestions(self, issues: List[Dict]) -> List[str]:
        """Generate improvement suggestions from issues"""
        suggestions = []
        
        high_priority_issues = [i for i in issues if i["severity"] == "high"]
        if high_priority_issues:
            suggestions.append("🔴 **Ưu tiên cao:** Cần sửa các vấn đề nghiêm trọng trước tiên.")
        
        grammar_issues = [i for i in issues if i["type"] == "grammar"]
        if grammar_issues:
            suggestions.append(f"📝 **Ngữ pháp:** Tìm thấy {len(grammar_issues)} lỗi ngữ pháp. Kiểm tra lại cấu trúc câu.")
        
        vocab_issues = [i for i in issues if i["type"] == "vocabulary"]
        if vocab_issues:
            suggestions.append(f"📚 **Từ vựng:** {len(vocab_issues)} từ không phù hợp. Cần thay bằng từ đơn giản hơn.")
        
        style_issues = [i for i in issues if i["type"] == "style"]
        if style_issues:
            suggestions.append(f"✍️ **Văn phong:** {len(style_issues)} vấn đề về văn phong. Câu có thể bị quá dài hoặc phức tạp.")
        
        if not issues:
            suggestions.append("✅ **Xuất sắc!** Nội dung của bạn rất tốt và phù hợp với độ tuổi mục tiêu.")
        
        return suggestions
    
    def improve_text(self, text: str, issues: List[Dict]) -> str:
        """Suggest improvements for specific issues"""
        improved_text = text
        
        # Sort issues by position (reverse order to protect indices)
        sorted_issues = sorted(issues, key=lambda x: x.get("position", 0), reverse=True)
        
        for issue in sorted_issues:
            if issue["type"] == "grammar" and "suggestion" in issue:
                # Replace text pattern with suggestion
                pattern = re.escape(issue["text_found"])
                improved_text = re.sub(pattern, issue["suggestion"], improved_text)
        
        return improved_text
    
    def generate_report(self, validation_results: Dict, format_type: str = "markdown") -> str:
        """Generate validation report"""
        lines = []
        
        # Summary
        lines.append("# Báo cáo Kiểm tra Tiếng Việt")
        lines.append("")
        lines.append(f"📊 **Điểm tổng thể:** {validation_results['overall_score']}/100")
        lines.append(f"📝 **Số từ:** {validation_results['word_count']}")
        lines.append(f"📄 **Số câu:** {validation_results['sentence_count']}")
        lines.append(f"👶 **Độ tuổi mục tiêu:** {validation_results['target_age']}")
        lines.append("")
        
        # Issues found
        if validation_results['issues']:
            lines.append("## Vấn đề phát hiện")
            lines.append("")
            
            # Group issues by type
            grammar_issues = [i for i in validation_results['issues'] if i['type'] == 'grammar']
            vocab_issues = [i for i in validation_results['issues'] if i['type'] == 'vocabulary']
            style_issues = [i for i in validation_results['issues'] if i['type'] == 'style']
            appropriate_issues = [i for i in validation_results['issues'] if i['type'] == 'appropriateness']
            
            if grammar_issues:
                lines.append("### Ngữ pháp")
                for issue in grammar_issues[:5]:  # Show first 5
                    lines.append(f"- ❌ **{issue['text_found']}**: {issue['message']}")
                    if issue.get('suggestion'):
                        lines.append(f"  💡 Gợi ý: {issue['suggestion']}")
                lines.append("")
            
            if vocab_issues:
                lines.append("### Từ vựng")
                for issue in vocab_issues[:5]:
                    lines.append(f"⚠️ **{issue['word']}**: {issue['message']}")
                lines.append("")
            
            if style_issues:
                lines.append("### Văn phong")
                for issue in style_issues[:3]:
                    lines.append(f"- 📝 Câu {issue['sentence_index']+1}: {issue['message']}")
                lines.append("")
            
            if appropriate_issues:
                lines.append("### Phù hợp độ tuổi")
                for issue in appropriate_issues:
                    lines.append(f"- 🚫 **{issue['word']}**: {issue['message']}")
                lines.append("")
        
        # Suggestions
        if validation_results['suggestions']:
            lines.append("## 📝 Gợi ý cải thiện")
            lines.append("")
            for suggestion in validation_results['suggestions']:
                lines.append(f"- {suggestion}")
            lines.append("")
        
        # Overall assessment
        lines.append("## 🎯 Đánh giá chung")
        score = validation_results['overall_score']
        if score >= 90:
            lines.append("✅ **Xuất sắc!** Nội dung của bạn rất chất lượng và phù hợp.")
        elif score >= 70:
            lines.append("👍 **Tốt!** Nội dung khá tốt, cần một vài thay đổi nhỏ.")
        elif score >= 50:
            lines.append("⚠️ **Trung bình.** Cần cải thiện một số điểm về ngữ pháp và văn phong.")
        else:
            lines.append("❌ **Cần cải thiện nhiều.** Nên xem xét lại toàn bộ nội dung.")
        
        return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Validate Vietnamese text")
    parser.add_argument("--input", help="Input file path")
    parser.add_argument("--text", help="Text to validate directly")
    parser.add_argument("--check", nargs="+", 
                       choices=["grammar", "vocabulary", "style", "appropriateness"],
                       default=["grammar", "vocabulary", "style", "appropriateness"])
    parser.add_argument("--target-age", default="elementary",
                       choices=["preschool", "elementary", "middle_grade", "young_adult"])
    parser.add_argument("--suggestions", action="store_true", help="Suggest improvements")
    parser.add_argument("--output", help="Output file for report")
    parser.add_argument("--format", default="markdown", choices=["markdown", "json"])
    parser.add_argument("--quick-check", action="store_true", help="Quick validation without detailed report")
    
    args = parser.parse_args()
    
    validator = VietnameseValidator()
    
    try:
        # Get text to validate
        if args.input:
            text = Path(args.input).read_text(encoding='utf-8')
        elif args.text:
            text = args.text
        else:
            print("Error: Provide either --input file or --text string")
            return 1
        
        # Validate text
        results = validator.validate_text(text, args.check, args.target_age)
        
        if args.quick_check:
            score = results["overall_score"]
            issue_count = len(results["issues"])
            print(f"Quick check: {issue_count} issues found, Score: {score}/100")
            return 0
        
        # Generate and output report
        if args.format == "markdown":
            report = validator.generate_report(results)
        else:
            report = json.dumps(results, ensure_ascii=False, indent=2)
        
        if args.output:
            Path(args.output).write_text(report, encoding='utf-8')
            print(f"Validation report saved to {args.output}")
        else:
            print(report)
        
        # Generate improved text if requested
        if args.suggestions and results["issues"]:
            improved = validator.improve_text(text, results["issues"])
            improved_file = Path("improved_" + (args.input or "text.txt"))
            improved_file.write_text(improved, encoding='utf-8')
            print(f"Improved text saved to {improved_file}")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
