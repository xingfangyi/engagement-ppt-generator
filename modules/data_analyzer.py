"""
Module to analyze engagement survey data and identify issues
"""

def analyze_data(ppt_data):
    """
    Analyze the parsed PPT data to identify key issues and trends
    
    Args:
        ppt_data: Dictionary containing parsed survey data
    
    Returns:
        dict: Analysis results including identified issues and recommendations
    """
    
    analysis = {
        'department': ppt_data['department'],
        'overall_score': round(ppt_data['overall_score'], 1) if ppt_data['overall_score'] else 0,
        'total_participants': ppt_data['total_participants'],
        'lowest_score': ppt_data['lowest_scores'][0] if ppt_data['lowest_scores'] else 0,
        'highest_score': ppt_data['highest_scores'][0] if ppt_data['highest_scores'] else 0,
        'score_range': {
            'low_end': ppt_data['lowest_scores'][0] if ppt_data['lowest_scores'] else 0,
            'high_end': ppt_data['highest_scores'][0] if ppt_data['highest_scores'] else 0,
        },
        'key_issues': [],
        'priority_areas': [],
    }
    
    # Identify key issues based on scores
    overall_score = analysis['overall_score']
    
    if overall_score < 75:
        analysis['key_issues'].append('Low employee engagement')
        analysis['priority_areas'].append('Sense of Belonging')
        analysis['priority_areas'].append('Work-Life Balance')
    
    # Check for specific low scores
    if analysis['lowest_score'] < 70:
        analysis['key_issues'].append('Critical low scores detected')
        if 'Belonging' not in analysis['priority_areas']:
            analysis['priority_areas'].append('Sense of Belonging')
    
    if not analysis['key_issues']:
        analysis['key_issues'].append('Room for improvement in employee satisfaction')
        analysis['priority_areas'] = ['Sense of Belonging', 'Work-Life Balance']
    
    # Add score distribution summary
    analysis['improvement_potential'] = 'High' if overall_score < 80 else 'Moderate' if overall_score < 90 else 'Stable'
    
    return analysis
