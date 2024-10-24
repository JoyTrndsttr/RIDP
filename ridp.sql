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

 Date: 08/10/2024 21:22:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for filecontents
-- ----------------------------
DROP TABLE IF EXISTS `filecontents`;
CREATE TABLE `filecontents`  (
  `ContentID` int(0) NOT NULL AUTO_INCREMENT,
  `FileID` int(0) NULL DEFAULT NULL,
  `Content` json NULL,
  PRIMARY KEY (`ContentID`) USING BTREE,
  INDEX `FileID`(`FileID`) USING BTREE,
  CONSTRAINT `filecontents_ibfk_1` FOREIGN KEY (`FileID`) REFERENCES `metrics` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2508 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for metrics
-- ----------------------------
DROP TABLE IF EXISTS `metrics`;
CREATE TABLE `metrics`  (
  `ID` int(0) NOT NULL AUTO_INCREMENT,
  `Bridge` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `FileName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ContentID` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `ContentID`(`ContentID`) USING BTREE,
  CONSTRAINT `metrics_ibfk_1` FOREIGN KEY (`ContentID`) REFERENCES `filecontents` (`ContentID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4036 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 342 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
