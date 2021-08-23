import setuptools


setuptools.setup(
    name="markerlessBoMI",
    version="1.0.0",
    author="Fabio Rizzoglio, Matteo Moro",
    author_email="matteo.moro@edu.unige.it",
    description="Toolbox to move computer cursor with body motion",
    long_description="Toolbox to move computer cursor with body motion",
    url="https://github.com/MoroMatteo/markerlessBoMI_FaMa.git",
    packages=setuptools.find_packages(),
    install_requires = ['absl-py==0.13.0',
#'actionlib==1.13.2',
'angles==1.9.13',
'astunparse==1.6.3',
'attrs==21.2.0',
'bondpy==1.8.6',
'cached-property==1.5.2',
'cachetools==4.2.2',
'camera-calibration==1.15.3',
'camera-calibration-parsers==1.12.0',
'catkin==0.8.10',
'certifi==2021.5.30',
'charset-normalizer==2.0.4',
'clang==5.0',
'controller-manager==0.19.5',
'controller-manager-msgs==0.19.5',
'cv-bridge==1.15.0',
'cycler==0.10.0',
'diagnostic-analysis==1.10.4',
'diagnostic-common-diagnostics==1.10.4',
'diagnostic-updater==1.10.4',
'dynamic-reconfigure==1.7.1',
'flatbuffers==1.12',
'gast==0.4.0',
'gazebo_plugins==2.9.2',
'gazebo_ros==2.9.2',
'gencpp==0.6.5',
'geneus==3.0.0',
'genlisp==0.4.18',
'genmsg==0.5.16',
'gennodejs==2.0.2',
'genpy==0.6.15',
'google-auth==1.35.0',
'google-auth-oauthlib==0.4.5',
'google-pasta==0.2.0',
'grpcio==1.39.0',
'h5py==3.1.0',
'idna==3.2',
'image-geometry==1.15.0',
'importlib-metadata==4.6.4',
'interactive-markers==1.12.0',
'joblib==1.0.1',
'joint_state_publisher==1.15.0',
'joint_state_publisher_gui==1.15.0',
'keras==2.6.0',
'Keras-Preprocessing==1.1.2',
'kiwisolver==1.3.1',
'laser_geometry==1.6.7',
'Markdown==3.3.4',
'matplotlib==3.4.3',
'mediapipe==0.8.7', #
'message-filters==1.15.11',
'MouseInfo==0.1.3',
'numpy==1.19.5',
'oauthlib==3.1.1',
'opencv-contrib-python==4.5.3.56',
'opencv-python==4.5.3.56',
'opt-einsum==3.3.0',
'pandas==1.3.2',
'Pillow==8.3.1',
'pip==21.2.4',
'protobuf==3.17.3',
'pyasn1==0.4.8',
'pyasn1-modules==0.2.8',
'PyAutoGUI==0.9.53',
'pygame==2.0.1',
'PyGetWindow==0.0.9',
'PyMsgBox==1.0.9',
'pyparsing==2.4.7',
'pyperclip==1.8.2',
'PyRect==0.1.4',
'PyScreeze==0.1.27',
'python-dateutil==2.8.2',
'python-qt-binding==0.4.4',
'python3-xlib==0.15',
'PyTweening==1.0.3',
'pytz==2021.1',
'qt-dotgraph==0.4.2',
'qt-gui==0.4.2',
'qt-gui-cpp==0.4.2',
'qt-gui-py-common==0.4.2',
'requests==2.26.0',
'requests-oauthlib==1.3.0',
'resource_retriever==1.12.6',
'rosbag==1.15.11',
'rosboost-cfg==1.15.7',
'rosclean==1.15.7',
'roscreate==1.15.7',
'rosgraph==1.15.11',
'roslaunch==1.15.11',
'roslib==1.15.7',
'roslint==0.12.0',
'roslz4==1.15.11',
'rosmake==1.15.7',
'rosmaster==1.15.11',
'rosmsg==1.15.11',
'rosnode==1.15.11',
'rosparam==1.15.11',
'rospy==1.15.11',
'rosservice==1.15.11',
'rostest==1.15.11',
'rostopic==1.15.11',
'rosunit==1.15.7',
'roswtf==1.15.11',
'rqt_action==0.4.9',
'rqt_bag==0.5.1',
'rqt_bag_plugins==0.5.1',
'rqt_console==0.4.11',
'rqt_dep==0.4.12',
'rqt_graph==0.4.14',
'rqt_gui==0.5.2',
'rqt_gui_py==0.5.2',
'rqt_image_view==0.4.16',
'rqt_launch==0.4.9',
'rqt_logger_level==0.4.11',
'rqt-moveit==0.5.10',
'rqt_msg==0.4.10',
'rqt_nav_view==0.5.7',
'rqt_plot==0.4.13',
'rqt_pose_view==0.5.11',
'rqt_publisher==0.4.10',
'rqt_py_common==0.5.2',
'rqt_py_console==0.4.10',
'rqt-reconfigure==0.5.4',
'rqt-robot-dashboard==0.5.8',
'rqt-robot-monitor==0.5.13',
'rqt_robot_steering==0.5.12',
'rqt_runtime_monitor==0.5.9',
'rqt-rviz==0.7.0',
'rqt_service_caller==0.4.10',
'rqt_shell==0.4.11',
'rqt_srv==0.4.9',
'rqt_tf_tree==0.6.2',
'rqt_top==0.4.10',
'rqt_topic==0.4.12',
'rqt_web==0.4.10',
'rsa==4.7.2',
'rviz==1.14.8',
'scikit-learn==0.24.2',
'scipy==1.7.1',
'sensor-msgs==1.13.1',
'setuptools==41.2.0',
'six==1.15.0',
'sklearn==0.0',
'smach==2.5.0',
'smach-ros==2.5.0',
'smclib==1.8.6',
'tensorboard==2.6.0',
'tensorboard-data-server==0.6.1',
'tensorboard-plugin-wit==1.8.0',
'tensorflow==2.6.0',
'tensorflow-estimator==2.6.0',
'termcolor==1.1.0',
'tf==1.13.2',
'tf-conversions==1.13.2',
'tf2-geometry-msgs==0.7.5',
'tf2-kdl==0.7.5',
'tf2-py==0.7.5',
'tf2-ros==0.7.5',
'threadpoolctl==2.2.0',
'topic-tools==1.15.11',
'typing-extensions==3.7.4.3',
'urllib3==1.26.6',
'Werkzeug==2.0.1',
'wheel==0.37.0',
'wrapt==1.12.1',
'xacro==1.14.8',
'zipp==3.5.0']    
)
