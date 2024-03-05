// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class KMSConfiguration {

  /**
   * Key Store only uses this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown.
   */
  private final String kmsKeyArn;

  /**
   * Key Store can use ANY KMS Key ARN. The VersionKey and CreateKey Operations will need the KMS Key ARN arguement set.
   */
  private final Discovery discovery;

  protected KMSConfiguration(BuilderImpl builder) {
    this.kmsKeyArn = builder.kmsKeyArn();
    this.discovery = builder.discovery();
  }

  /**
   * @return Key Store only uses this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown.
   */
  public String kmsKeyArn() {
    return this.kmsKeyArn;
  }

  /**
   * @return Key Store can use ANY KMS Key ARN. The VersionKey and CreateKey Operations will need the KMS Key ARN arguement set.
   */
  public Discovery discovery() {
    return this.discovery;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param kmsKeyArn Key Store only uses this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown.
     */
    Builder kmsKeyArn(String kmsKeyArn);

    /**
     * @return Key Store only uses this KMS Key ARN. If a different KMS Key ARN is encountered when creating, versioning, or getting a Branch Key or Beacon Key, KMS is never called and an exception is thrown.
     */
    String kmsKeyArn();

    /**
     * @param discovery Key Store can use ANY KMS Key ARN. The VersionKey and CreateKey Operations will need the KMS Key ARN arguement set.
     */
    Builder discovery(Discovery discovery);

    /**
     * @return Key Store can use ANY KMS Key ARN. The VersionKey and CreateKey Operations will need the KMS Key ARN arguement set.
     */
    Discovery discovery();

    KMSConfiguration build();
  }

  static class BuilderImpl implements Builder {

    protected String kmsKeyArn;

    protected Discovery discovery;

    protected BuilderImpl() {}

    protected BuilderImpl(KMSConfiguration model) {
      this.kmsKeyArn = model.kmsKeyArn();
      this.discovery = model.discovery();
    }

    public Builder kmsKeyArn(String kmsKeyArn) {
      this.kmsKeyArn = kmsKeyArn;
      return this;
    }

    public String kmsKeyArn() {
      return this.kmsKeyArn;
    }

    public Builder discovery(Discovery discovery) {
      this.discovery = discovery;
      return this;
    }

    public Discovery discovery() {
      return this.discovery;
    }

    public KMSConfiguration build() {
      if (Objects.nonNull(this.kmsKeyArn()) && this.kmsKeyArn().length() < 1) {
        throw new IllegalArgumentException(
          "The size of `kmsKeyArn` must be greater than or equal to 1"
        );
      }
      if (
        Objects.nonNull(this.kmsKeyArn()) && this.kmsKeyArn().length() > 2048
      ) {
        throw new IllegalArgumentException(
          "The size of `kmsKeyArn` must be less than or equal to 2048"
        );
      }
      if (!onlyOneNonNull()) {
        throw new IllegalArgumentException(
          "`KMSConfiguration` is a Union. A Union MUST have one and only one value set."
        );
      }
      return new KMSConfiguration(this);
    }

    private boolean onlyOneNonNull() {
      Object[] allValues = { this.kmsKeyArn, this.discovery };
      boolean haveOneNonNull = false;
      for (Object o : allValues) {
        if (Objects.nonNull(o)) {
          if (haveOneNonNull) {
            return false;
          }
          haveOneNonNull = true;
        }
      }
      return haveOneNonNull;
    }
  }
}
