from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    irb1300_urdf_path = get_package_share_directory("irb1300_urdf")
    urdf_file = irb1300_urdf_path + "/urdf/1300_urdf.urdf"
    rviz_config_file = irb1300_urdf_path + "/config/display.rviz"
    
    robot_description = ParameterValue(Command(['xacro ', urdf_file]), value_type=str)
    
    return LaunchDescription([
        DeclareLaunchArgument(
            name='model',
            default_value=urdf_file
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file]
        )
    ])
