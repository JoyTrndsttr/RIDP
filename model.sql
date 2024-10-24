/*
 Navicat Premium Data Transfer

 Source Server         : Database
 Source Server Type    : MySQL
 Source Server Version : 80039
 Source Host           : localhost:3306
 Source Schema         : ridp

 Target Server Type    : MySQL
 Target Server Version : 80039
 File Encoding         : 65001

 Date: 09/10/2024 21:50:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for model
-- ----------------------------
DROP TABLE IF EXISTS `model`;
CREATE TABLE `model`  (
  `ModelID` int(0) NOT NULL AUTO_INCREMENT,
  `Type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ModelType` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Parameters` json NULL,
  PRIMARY KEY (`ModelID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 343 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of model
-- ----------------------------
INSERT INTO `model` VALUES (286, 'ZZWY1', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (287, 'ZZWY1', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (288, 'ZZWY1', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (289, 'ZZWY2', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (290, 'ZZWY2', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (291, 'ZZWY2', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (292, 'ZZWY3', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (293, 'ZZWY3', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (294, 'ZZWY3', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (295, 'ZZWY4', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (296, 'ZZWY4', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (297, 'ZZWY4', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (298, 'LFWY', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (299, 'LFWY', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (300, 'LFWY', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (301, 'ZDJSD2', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (302, 'ZDJSD2', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (303, 'ZDJSD2', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (304, 'ZDWY2', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (305, 'ZDWY2', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (306, 'ZDWY2', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (307, 'ZDJSD1', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (308, 'ZDJSD1', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (309, 'ZDJSD1', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (310, 'ZDWY1', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (311, 'ZDWY1', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (312, 'ZDWY1', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (313, 'LDQJ', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (314, 'LDQJ', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (315, 'LDQJ', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (316, 'WD', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (317, 'WD', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (318, 'WD', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (319, 'SD', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (320, 'SD', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (321, 'SD', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (322, 'SXJSDX', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (323, 'SXJSDX', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (324, 'SXJSDX', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (325, 'XDWY1', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (326, 'XDWY1', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (327, 'XDWY1', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (328, 'XDWY2', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (329, 'XDWY2', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (330, 'XDWY2', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (331, 'SXJSDZ', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (332, 'SXJSDZ', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (333, 'SXJSDZ', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (334, 'SXJSDY', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (335, 'SXJSDY', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (336, 'SXJSDY', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (337, 'DND', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (338, 'DND', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (339, 'DND', 'FilterModel', '{\"window_size\": 100}');
INSERT INTO `model` VALUES (340, 'DYB', 'CleanModel', '{\"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (341, 'DYB', 'CutModel', '{\"extension\": 0.05, \"threshold\": [0.01, 0.01, 0.01, 0.01]}');
INSERT INTO `model` VALUES (342, 'DYB', 'FilterModel', '{\"window_size\": 100}');

SET FOREIGN_KEY_CHECKS = 1;
