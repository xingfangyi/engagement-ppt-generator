"""
Module to generate improvement suggestions based on analysis
"""

BELONGING_SUGGESTIONS = [
    "Organize annual family events such as company dinners including family members",
    "Arrange regular site visits by Sales and Project Managers to listen to employee feedback",
    "Continue to provide safety and resilience training programs",
    "Arrange alternative team-building activities for employees unable to attend main events",
    "Provide timely and appropriate recognition for individuals with extra contributions",
    "Share best practices, success stories, and lessons learned across the team",
]

WORK_LIFE_BALANCE_SUGGESTIONS = [
    "Assess available time windows for maintenance during sales phases to avoid excessive overtime",
    "Project Managers proactively communicate with customers to manage workload expectations",
    "Arrange monthly home visits for site engineers to support well-being",
    "Assign service sites closer to service engineers' homes to reduce commute time",
    "Review annual leave quarterly and ensure all annual leave is fully utilized by year-end",
    "Offer diverse recognition and celebrate achievements through inclusive activities",
]

LEADERSHIP_SUGGESTIONS = [
    "Implement leadership development programs to support implementation of improvement initiatives",
    "Enhance manager capabilities in supporting team well-being and sense of belonging",
    "Provide coaching and mentoring training for managers and team leaders",
    "Establish regular feedback mechanisms between management and team members",
]

def generate_suggestions(analysis):
    """
    Generate improvement suggestions based on analysis results
    
    Args:
        analysis: Dictionary containing analysis results
    
    Returns:
        dict: Improvement suggestions organized by category
    """
    
    suggestions = {
        'belonging': BELONGING_SUGGESTIONS.copy(),
        'work_life_balance': WORK_LIFE_BALANCE_SUGGESTIONS.copy(),
        'leadership': LEADERSHIP_SUGGESTIONS.copy(),
        'total_actions': len(BELONGING_SUGGESTIONS) + len(WORK_LIFE_BALANCE_SUGGESTIONS),
        'priority_areas': analysis.get('priority_areas', []),
    }
    
    # Customize suggestions based on analysis
    if analysis['improvement_potential'] == 'High':
        # Add extra suggestions for departments with low scores
        suggestions['additional_notes'] = (
            "High priority needed: Multiple areas require immediate attention. "
            "Recommend starting with quick wins in team engagement and schedule flexibility."
        )
    else:
        suggestions['additional_notes'] = (
            "Good baseline engagement. Focus on continuous improvement in identified areas."
        )
    
    return suggestions
